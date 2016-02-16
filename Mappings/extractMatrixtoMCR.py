#!/usr/bin/python

import textwrap, argparse

from collections import defaultdict

if __name__ == '__main__':

	parserarg = argparse.ArgumentParser(
	     prog='extractMatrixtoMCR.py',
	     formatter_class=argparse.RawDescriptionHelpFormatter,
	     description=textwrap.dedent('''\
		 Extract data from Matrix to export data to MCR, change csco from the selected synset-variants
		 --------------------------------
		     example of use $python3 %(prog)s --file_matrix matrix.tab
		 '''))

	parserarg.add_argument('--file_matrix', dest='file_matrix', required=True, type=str , help='matrix\'s file (required)')

	args = parserarg.parse_args()

	### Read and Create matrix ################################################

	input_file_matrix = open(args.file_matrix, "r")
	line = input_file_matrix.readline()

	header = line.split()
	lex_names = line.split()[3:]

	cnt_99 = 0
	cnt_rev = 0
	cnt_up49_ok = 0
	cnt_up49_ko = 0
	cnt_up00_ok = 0
	cnt_up00_ko = 0
	cnt_n1_ok = 0
	cnt_n1_ko = 0
	cnt_n_oth = 0

	mat = defaultdict(dict)

	for line in input_file_matrix.readlines():

		# recovery first three values, synset, variant and csco
		syn,word,csco_tmp = line.split()[:3]
		csco = float(csco_tmp)

		ok_rev = 0
		for idx,elem in enumerate(line.split()[3:]):
			if elem != '0' and lex_names[idx] == 'revisats':
				ok_rev = 1

		# Case 0a: IF csco>=99 only count it
		if csco >= 99:

			select = '99'
			cnt_99 = cnt_99 + 1

		# Case 0b: Catalan, "Revisats" (cat: 12042) 
		elif ok_rev == 1:

			select = 'rev'
			cnt_rev = cnt_rev + 1

		# Case 0c: IF csco>49 and not present in other "resource" or "language" THEN csco not change (spa: 72546 // cat:71706 // eus:50039)
		elif csco > 49 :

			ko = 1
			# recovery other data present in the file, and check that some not is 0's
			for elem in line.split()[3:]:
				if elem != '0':
					ko = 0
			if ko == 1:
				select = 'up49_ko'
				cnt_up49_ko = cnt_up49_ko + 1
			else:
				select = 'up49_ok'
				cnt_up49_ok = cnt_up49_ok + 1

		# Case 1: IF csco>=0 and it's present in other "resource" or "language" THEN csco up to 99 (spa: 17534 // cat: 149)
		elif csco >= 0 :

			ko = 1
			# recovery other data present in the file, and check that all are 0's
			for elem in line.split()[3:]:
				if elem != '0':
					ko = 0
			if ko == 1:
				select = 'up00_ko'
				cnt_up00_ko = cnt_up00_ko + 1
			else:
				select = 'up00_ok'
				cnt_up00_ok = cnt_up00_ok + 1

		# Case 2: IF csco==-1 and it's present in any "resource" (not babelnet) and in some "language" THEN csco up to 99 (?)
		elif csco == -1:

			ok_lng = 0
			ok_rcs = 0
			babelnet = 0
			# recovery other data present in the file, and check that all are 0's
			for idx,elem in enumerate(line.split()[3:]):
				if elem != '0':
					if "_cl" in lex_names[idx]:
						ok_lng = 1
					elif lex_names[idx] != 'babelnet':
						ok_rcs = 1

			if ok_lng and ok_rcs:
				select = 'n1_ok'
				cnt_n1_ok = cnt_n1_ok + 1
			else:
				select = 'n1_ko'
				cnt_n1_ko = cnt_n1_ko + 1

		# Case 3: IF csco<-1 THEN csco up to 99 (spa: 11866 // cat: 3056 // eus:1575)
		elif csco < -1:
				select = 'n_oth'
				cnt_n_oth = cnt_n_oth + 1
		else:
			print "Case not present, exit"
			print line
			exit()

		try:
			if word not in mat[select][syn]:
				mat[select].setdefault(syn,[]).append(word)

		except KeyError:
			mat[select].setdefault(syn,[]).append(word)

	input_file_matrix.close()
	out_name,ext = args.file_matrix.split(".")
	lang = out_name.split("-")[:2]

	list_sel = ['n1_ok','n_oth','up00_ok','up49_ok','rev']

	for sel,values in mat.items():

		output_file = open(out_name+'_'+sel+'.'+ext, "w")

		if sel in list_sel:
			output_file_sql = open(out_name+'_'+sel+'.sql', "w")

		for syn,words in values.items():
			for word in words:
				output_file.write(syn+"\t"+word+"\n")

				if sel in list_sel:
					output_file_sql.write("UPDATE `wei_"+lang+"_variant` SET `csco`=99 WHERE `offset` LIKE '"+lang+"-"+syn+"' AND `word` LIKE '"+word+"';\n")

		output_file.close()

		if sel in list_sel:
			output_file_sql.close()

	print "\nCNT 99:\t\t"+str(cnt_99)+"\n"
	print "CNT REV:\t"+str(cnt_rev)+"\n"
	print "CNT >49 OK:\t"+str(cnt_up49_ok)+"\n"
	print "CNT >49 KO:\t"+str(cnt_up49_ko)+"\n"
	print "CNT >00 OK:\t"+str(cnt_up00_ok)+"\n"
	print "CNT >00 KO:\t"+str(cnt_up00_ko)+"\n"
	print "CNT  -1 OK:\t"+str(cnt_n1_ok)+"\n"
	print "CNT  -1 KO:\t"+str(cnt_n1_ko)+"\n"
	print "CNT < -1:\t"+str(cnt_n_oth)+"\n"
