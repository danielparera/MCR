#!/bin/bash          

echo Update Euskera Matrix with lexicon resources
mv out/matrix-eus-30DB.tab out/matrix-eus-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-eus-30_0.tab --file_lexicon data/wn-cldr-eus.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-eus-30_1.tab --file_lexicon data/wn-wikt-eus.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-eus-30_2.tab --file_lexicon data/uwn-eus.txt --new_field_name UWN
python3 updateMatrix.py --file_matrix out/matrix-eus-30_3.tab --file_lexicon data/VariantsFromPM_eus.txt --new_field_name PM
python3 updateMatrix.py --file_matrix out/matrix-eus-30_4.tab --file_lexicon data/wn-torevise-eus.txt --new_field_name torevise

echo Update English Matrix with lexicon resources
mv out/matrix-eng-30DB.tab out/matrix-eng-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-eng-30_0.tab --file_lexicon data/wn-cldr-eng.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-eng-30_1.tab --file_lexicon data/wn-wikt-eng.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-eng-30_2.tab --file_lexicon data/uwn-eng.txt --new_field_name UWN
python3 updateMatrix.py --file_matrix out/matrix-eng-30_3.tab --file_lexicon data/VariantsFromPM_eng.txt --new_field_name PM

echo Update Spanish Matrix with lexicon resources
mv out/matrix-spa-30DB.tab out/matrix-spa-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-spa-30_0.tab --file_lexicon data/wn-cldr-spa.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-spa-30_1.tab --file_lexicon data/wn-wikt-spa.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-spa-30_2.tab --file_lexicon data/uwn-spa.txt --new_field_name UWN
python3 updateMatrix.py --file_matrix out/matrix-spa-30_3.tab --file_lexicon data/VariantsFromPM_spa.txt --new_field_name PM
python3 updateMatrix.py --file_matrix out/matrix-spa-30_4.tab --file_lexicon data/wn-torevise-spa.txt --new_field_name torevise
python3 updateMatrix.py --file_matrix out/matrix-spa-30_5.tab --file_lexicon data/ancora.spa --new_field_name ancora
python3 updateMatrix.py --file_matrix out/matrix-spa-30_6.tab --file_lexicon data/wordnet-babelnet.es.v4.txt --new_field_name babelnet
python3 updateMatrix.py --file_matrix out/matrix-spa-30_7.tab --file_lexicon data/fase1.txt --new_field_name fase1
python3 updateMatrix.py --file_matrix out/matrix-spa-30_8.tab --file_lexicon data/fase2.txt --new_field_name fase2

echo Update Catalan Matrix with lexicon resources
mv out/matrix-cat-30DB.tab out/matrix-cat-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-cat-30_0.tab --file_lexicon data/wn-cldr-cat.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-cat-30_1.tab --file_lexicon data/wn-wikt-cat.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-cat-30_2.tab --file_lexicon data/uwn-cat.txt --new_field_name UWN
python3 updateMatrix.py --file_matrix out/matrix-cat-30_3.tab --file_lexicon data/VariantsFromPM_cat.txt --new_field_name PM
python3 updateMatrix.py --file_matrix out/matrix-cat-30_4.tab --file_lexicon data/wn-torevise-cat.txt --new_field_name torevise
python3 updateMatrix.py --file_matrix out/matrix-cat-30_5.tab --file_lexicon data/revisats-cat.txt --new_field_name revisats
python3 updateMatrix.py --file_matrix out/matrix-cat-30_6.tab --file_lexicon data/ancora.cat --new_field_name ancora
python3 updateMatrix.py --file_matrix out/matrix-cat-30_7.tab --file_lexicon data/wordnet-babelnet.ca.v4.txt --new_field_name babelnet

echo Update Galician Matrix with lexicon resources
mv out/matrix-glg-30DB.tab out/matrix-glg-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-glg-30_0.tab --file_lexicon data/wn-cldr-glg.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-glg-30_1.tab --file_lexicon data/wn-wikt-glg.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-glg-30_2.tab --file_lexicon data/uwn-glg.txt --new_field_name UWN
python3 updateMatrix.py --file_matrix out/matrix-glg-30_3.tab --file_lexicon data/wn-torevise-glg.txt --new_field_name torevise

echo Update Portuguese Matrix with lexicon resources
mv out/matrix-por-30DB.tab out/matrix-por-30_0.tab
python3 updateMatrix.py --file_matrix out/matrix-por-30_0.tab --file_lexicon data/wn-cldr-por.tab --new_field_name EOWN-cldr
python3 updateMatrix.py --file_matrix out/matrix-por-30_1.tab --file_lexicon data/wn-wikt-por.tab --new_field_name EOWN-wikt
python3 updateMatrix.py --file_matrix out/matrix-por-30_2.tab --file_lexicon data/uwn-por.txt --new_field_name UWN


echo Update Euskera Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-eus-30_5.tab --file_lexicon out/matrix-eng-30_4.tab --new_field_name eng --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eus-30_6.tab --file_lexicon out/matrix-spa-30_9.tab --new_field_name spa --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eus-30_7.tab --file_lexicon out/matrix-cat-30_8.tab --new_field_name cat --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eus-30_8.tab --file_lexicon out/matrix-glg-30_4.tab --new_field_name glg --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eus-30_9.tab --file_lexicon out/matrix-por-30_3.tab --new_field_name por --cross_lingual

echo Update English Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-eng-30_4.tab --file_lexicon out/matrix-eus-30_5.tab --new_field_name eus --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eng-30_5.tab --file_lexicon out/matrix-spa-30_9.tab --new_field_name spa --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eng-30_6.tab --file_lexicon out/matrix-cat-30_8.tab --new_field_name cat --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eng-30_7.tab --file_lexicon out/matrix-glg-30_4.tab --new_field_name glg --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-eng-30_8.tab --file_lexicon out/matrix-por-30_3.tab --new_field_name por --cross_lingual

echo Update Spanish Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-spa-30_9.tab --file_lexicon out/matrix-eus-30_5.tab --new_field_name eus --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-spa-30_10.tab --file_lexicon out/matrix-eng-30_4.tab --new_field_name eng --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-spa-30_11.tab --file_lexicon out/matrix-cat-30_8.tab --new_field_name cat --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-spa-30_12.tab --file_lexicon out/matrix-glg-30_4.tab --new_field_name glg --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-spa-30_13.tab --file_lexicon out/matrix-por-30_3.tab --new_field_name por --cross_lingual

echo Update Catalan Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-cat-30_8.tab  --file_lexicon out/matrix-eus-30_5.tab --new_field_name eus --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-cat-30_9.tab  --file_lexicon out/matrix-eng-30_4.tab --new_field_name eng --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-cat-30_10.tab  --file_lexicon out/matrix-spa-30_9.tab --new_field_name spa --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-cat-30_11.tab  --file_lexicon out/matrix-glg-30_4.tab --new_field_name glg --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-cat-30_12.tab --file_lexicon out/matrix-por-30_3.tab --new_field_name por --cross_lingual

echo Update Galician Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-glg-30_4.tab --file_lexicon out/matrix-eus-30_5.tab --new_field_name eus --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-glg-30_5.tab --file_lexicon out/matrix-eng-30_4.tab --new_field_name eng --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-glg-30_6.tab --file_lexicon out/matrix-spa-30_9.tab --new_field_name spa --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-glg-30_7.tab --file_lexicon out/matrix-cat-30_8.tab --new_field_name cat --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-glg-30_8.tab --file_lexicon out/matrix-por-30_3.tab --new_field_name por --cross_lingual

echo Update Portuguese Matrix with other languages
python3 updateMatrix.py --file_matrix out/matrix-por-30_3.tab --file_lexicon out/matrix-eus-30_5.tab --new_field_name eus --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-por-30_4.tab --file_lexicon out/matrix-eng-30_4.tab --new_field_name eng --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-por-30_5.tab --file_lexicon out/matrix-spa-30_9.tab --new_field_name spa --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-por-30_6.tab --file_lexicon out/matrix-cat-30_8.tab --new_field_name cat --cross_lingual
python3 updateMatrix.py --file_matrix out/matrix-por-30_7.tab --file_lexicon out/matrix-glg-30_4.tab --new_field_name glg --cross_lingual


echo Clean and Move
mv out/matrix-eus-30_10.tab out/matrix-eus-30.tab
mv out/matrix-eus-30_0.tab out/matrix-eus-30DB.tab
rm out/matrix-eus-30_*.tab

mv out/matrix-eng-30_9.tab out/matrix-eng-30.tab
mv out/matrix-eng-30_0.tab out/matrix-eng-30DB.tab
rm out/matrix-eng-30_*.tab

mv out/matrix-spa-30_14.tab out/matrix-spa-30.tab
mv out/matrix-spa-30_0.tab out/matrix-spa-30DB.tab
rm out/matrix-spa-30_*.tab

mv out/matrix-cat-30_13.tab out/matrix-cat-30.tab
mv out/matrix-cat-30_0.tab out/matrix-cat-30DB.tab
rm out/matrix-cat-30_*.tab

mv out/matrix-glg-30_9.tab out/matrix-glg-30.tab
mv out/matrix-glg-30_0.tab out/matrix-glg-30DB.tab
rm out/matrix-glg-30_*.tab

mv out/matrix-por-30_8.tab out/matrix-por-30.tab
mv out/matrix-por-30_0.tab out/matrix-por-30DB.tab
rm out/matrix-por-30_*.tab

ls -lrt out

echo Extract information from Euskera matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-eus-30.tab --stats_info --log_files

echo Extract information from Catalan matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-cat-30.tab --stats_info --valid_list revisats --log_files

echo Extract information from Spanish matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-spa-30.tab --stats_info --valid_list fase1 --log_files

echo Extract information from Galician matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-glg-30.tab --stats_info --log_files

echo Extract information from English matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-eng-30.tab --stats_info --log_files

echo Extract information from Portuguese matrix
python3 extractMatrixtoMCR.py --file_matrix out/matrix-por-30.tab --stats_info --log_files
