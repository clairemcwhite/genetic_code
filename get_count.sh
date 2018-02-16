BLA=$1

#grep -Ff six_or_more.txt ../proteome/human_proteome.fasta 


while read x
do

count=`grep -o $x proteome/human_proteinstring.txt | wc -l`

if [ ! $count -eq 0 ]
then 
echo $x $count
fi


done < $BLA

