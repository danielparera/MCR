#!/usr/bin/python

import time
import subprocess, os
import textwrap, argparse
import pymysql

#can use this also
#import MySQLdb

parserarg = argparse.ArgumentParser(
     prog='buildUpdateOMW.py',
     formatter_class=argparse.RawDescriptionHelpFormatter,
     description=textwrap.dedent('''\
         check MCR with OMW datasets
         --------------------------------
             example of use $python3 %(prog)s --host host --db database --user user --pwd password
         '''))

parserarg.add_argument('--host', dest='host_db', required=True, type=str , help='host url\'s database (required)')
parserarg.add_argument('--user', dest='user_db', required=True, type=str , help='user\'s database (required)')
parserarg.add_argument('--pwd', dest='pwd_db', required=True, type=str , help='password\'s database (required)')
parserarg.add_argument('--db', dest='db_db', required=True, type=str , help='database\'s selection (required)')

parserarg.add_argument('--t', dest='t', required=False, default='wikt', type=str , help='file type (cldr/wikt)')
parserarg.add_argument('--l', dest='l', action='append', required=False, type=str , help='language (default all)')

args = parserarg.parse_args()

languages_user = args.l
t = args.t

# if not define language, explore all by default.
if not languages_user: languages_user = ['cat-30','eus-30', 'eng-30', 'spa-30', 'glg-30']

if not t == 'cldr' and not t == 'wikt':
	print("t parameter must be 'wikt' or 'cldr'")
	exit(1)

#choose one of them
#db = MySQLdb.connect(host=args.host_db, user=args.user_db, passwd=args.pwd_db, db=args.db_db) 
#cur = db.cursor(MySQLdb.cursors.DictCursor) 

db = pymysql.connect(host=args.host_db, user=args.user_db, passwd=args.pwd_db, db=args.db_db) 
cur = db.cursor(pymysql.cursors.DictCursor) 

cur.execute("select * FROM wei_languages")
rows = cur.fetchall()

# we build lists of file_outputs.
languages_mcr = []
for row in rows: languages_mcr.append(row["code"])

print "LANGUAGES MCR: "+str(languages_mcr)
print "LANGUAGES USER: "+str(languages_user)

if not os.path.exists('out'):
	os.makedirs('out')

for lang in languages_user:

	if lang in languages_mcr:

		sense = {}

		lng = lang.split("-")[0]
		print("OPEN FILES FOR LANGUAGE "+lng)
		
		input_file = open('data/wn-'+t+'-'+lng+'.tab', "r")
		output_file_upd = open('out/updateCS-'+t+'-'+lng+'.tab', "w")
		output_file_sql = open('out/updateCS-'+t+'-'+lng+'.sql', "w")

		for idx,line in enumerate(input_file.readlines()):

			li=line.strip()
			if not li.startswith("#"):

				if(len(li.split("\t")) == 3):	

					syn,lemma,word = li.split("\t")

					p = "SYN:"+syn+"\tW:"+word

					wtmp = word.replace("'","\\'") # get information from OMW file and make a sql with it (synset,word)
					w = wtmp.replace(" ","_")
					#ws = wtmp.replace(" ","\_") # scape underscore, in like SQL sentence underscore is wildcard (any caracter)

					sql_ili = "SELECT * FROM `wei_"+lang+"_to_ili` WHERE `offset` LIKE '"+lang+"-"+syn+"'"
					sql_var = "SELECT * FROM `wei_"+lang+"_variant` WHERE `offset` LIKE '"+lang+"-"+syn+"'"
					sql_w = sql_var+" AND `word` = '"+w+"'"
					cur.execute(sql_w+" AND `csco` = 99")
					rows_99 = cur.fetchall()
					cur.execute(sql_w+" AND `csco` < 99 AND `csco` > 49")
					rows_49to99 = cur.fetchall()
					cur.execute(sql_w+" AND `csco` <= 49")
					rows_49 = cur.fetchall()

					cur.execute(sql_var)
					rows_var = cur.fetchall()
					cur.execute(sql_ili)
					rows_ili = cur.fetchall()

					# only one result for word and synset in MCR 
					if len(rows_99) == 1:

						for row in rows_99:

							#print "NOTHING TO DO IN MCR"
							output_file_upd.write("99\t"+syn + "\t"+str(row['csco'])+"\t"+w+"\n")

					# more than one result for word and synset in MCR
					elif len(rows_99) > 1:

							print rows_99

							print "ERROR SYNSET 99:"+syn
							exit(1)

					elif len(rows_49to99) == 1:

						for row in rows_49to99:

							#print (p + "\tCS: "+str(row['csco'])+"\tSTS:"+str(row['status'])+"\tW:"+row['word']+"\n")
							output_file_upd.write("74\t"+syn + "\t"+str(row['csco'])+"\t"+w+"\n")
							output_file_sql.write("UPDATE `wei_"+lang+"_variant` SET `csco`=99 WHERE `offset` LIKE '"+lang+"-"+syn+"' AND `word` LIKE '"+w+"';\n")

					elif len(rows_49to99) > 1:

							print rows_49to99

							print "ERROR SYNSET 49 to 99:"+syn
							exit(1)

					elif len(rows_49) == 1:

						for row in rows_49:

							#print (p + "\tCS: "+str(row['csco'])+"\tSTS:"+str(row['status'])+"\tW:"+row['word']+"\n")
							output_file_upd.write("49\t"+syn + "\t"+str(row['csco'])+"\t"+w+"\n")
							output_file_sql.write("UPDATE `wei_"+lang+"_variant` SET `csco`=94 WHERE `offset` LIKE '"+lang+"-"+syn+"' AND `word` LIKE '"+w+"';\n")

					elif len(rows_49) > 1:

							print rows_49

							print "ERROR SYNSET 49:"+syn
							exit(1)

					elif len(rows_ili) == 1:

						pos = syn.split('-')[1]

						# get maximum sense value, if exist (same synset, diferent variant/word) add 1 to last sense. 
						if syn in sense:
							sense[syn] += 1
						else:
							sense[syn] = 0

							for row in rows_var:
								#print "s:"+str(sense)
								#print "r:"+str(row['sense'])
								if row['sense'] > sense[syn]: sense[syn] = row['sense']

							sense[syn] += 1

						#print "S:"+str(sense)
						#print (p + "\tCS: "+str(row['csco'])+"\tSTS:"+str(row['status'])+"\tW:"+row['word']+"\n")
						output_file_upd.write("NW\t"+syn + "\t94.0\t"+w+"\n")
						output_file_sql.write("INSERT INTO `wei_"+lang+"_variant` (`word`,`sense`,`offset`,`pos`,`csco`) VALUES ('"+w+"',"+str(sense[syn])+",'"+lang+"-"+syn+"',"+pos+",94);\n")
					else:
							print rows_ili

							print "ERROR, not only one result or no result. SYNSET ILI:"+syn
							#exit(1)

		print "\nStart: "+time.strftime("%H:%M:%S %d/%m/%y \n")

		cmd_o = "gawk 'BEGIN{FS=\"\\t\"}{print $2,$4}' out/updateCS-"+t+"-"+lng+".tab | tr _ ' ' | sed \"s/\\\\\\'/'/g\" > out/o_"+t+"-"+lng+".cmp"

		cmd_o_sort = "gawk 'BEGIN{FS=\"\\t\"}{print $2,$4}' out/updateCS-"+t+"-"+lng+".tab | tr _ ' ' | sed \"s/\\\\\\'/'/g\" | sort > out/o_"+t+"-"+lng+"_sort.cmp"

		print "Execute: "+cmd_o
		subprocess.call(cmd_o, shell=True)

		print "Execute: "+cmd_o_sort
		subprocess.call(cmd_o_sort, shell=True)

		cmd_d = "gawk 'BEGIN{FS=\"\\t\"}{print $1,$3}' data/wn-"+t+"-"+lng+".tab > out/d_"+t+"-"+lng+".cmp"

		cmd_d_sort = "gawk 'BEGIN{FS=\"\\t\"}{print $1,$3}' data/wn-"+t+"-"+lng+".tab | sort > out/d_"+t+"-"+lng+"_sort.cmp"

		print "Execute: "+cmd_d
		subprocess.call(cmd_d, shell=True)

		print "Execute: "+cmd_d_sort
		subprocess.call(cmd_d_sort, shell=True)

		cmd_c = 'comm out/d_'+t+'-'+lng+'_sort.cmp out/o_'+t+'-'+lng+'_sort.cmp -3'

		print "Execute: "+cmd_c
		print subprocess.check_output(cmd_c, shell=True)

		print "Finish: "+time.strftime("%H:%M:%S %d/%m/%y \n")

		input_file.close()
		output_file_upd.close()
		output_file_sql.close()
		print("CLOSE FILES FOR LANGUAGE "+lng)