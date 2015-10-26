#for f in ~/genetic_code/proteomes/*.fasta; do echo $f; python word_checker.py ../dictionaries/nine_or_more.txt $f nine_all_euks.txt; done

for f in ~/genetic_code/proteomes/UP000005640_9606.fasta; do echo $f; python word_checker.py CheckNames.txt $f frivolous.txt; done










