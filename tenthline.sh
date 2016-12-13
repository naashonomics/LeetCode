#Tenth Line

#For example, assume that file.txt has the following content:

#Line 1
#Line 2
#Line 3
#Line 4
#Line 5
#Line 6
#Line 7
#Line 8
#Line 9
#Line 10
#Your script should output the tenth line, which is:
#Line 10

file.txt=$1

#solution1 : using awk
awk 'NR==10{print $0}' $file.txt

#solution 2 : using sed 
sed -n "10p" $file.txt 
 


