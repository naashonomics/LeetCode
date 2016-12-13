#Word Frequency

#Write a bash script to calculate the frequency of each word in a text file words.txt.

#For simplicity sake, you may assume:  words.txt contains only lowercase characters and space ' ' characters. Each word must consist of lowercase characters only. Words are separated by one or more whitespace characters.For example, assume that words.txt has the following content:
#the day is sunny the the
#the sunny is is

#Your script should output the following, sorted by descending frequency:
#the 4
#is 3
#sunny 2
#day 1

file.txt=$1

cat "$file.txt" | tr -s "\t| " "\n" | sort | uniq -c | sort -k 1 -r | awk '{print $2,$1}'  
 


