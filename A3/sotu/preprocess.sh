#!/bin/bash

# The original source file  was copied to: orig.txt
cp stateoftheunion1790-2017.txt orig.txt

# Remove Trailing comment
# sed 178754d orig.txt > origA.txt
sed -i "" 179400d orig.txt

# Remove Header lines from file
# sed 1,241d origA.txt > orig_headless.txt
sed -i "" 1,244d orig.txt

# // get line numbers of where to split
# grep -Fn '***' orig.txt | cut -f1 -d: 

# Use perl script to split all speeches into individual files:
#  Script adapted from: http://stackoverflow.com/questions/8061475/split-one-file-into-multiple-files-based-on-pattern
./split.pl orig.txt

mkdir -p step1
mv a* step1/.

# For every speech do some additional preprocessing
cd step1
for i in a*
do
	sed -i "" 1,5d $i
done

cd ..
mkdir -p step2

# Run R script to do further text pre-processing
Rscript text-preprocess-2017.R

# Take the preprocessed files with the punctuation and numbers removed and convert them to be 
#  one word per line
#  http://unix.stackexchange.com/questions/79413/using-sed-how-to-format-one-word-per-line-removing-white-space

mkdir -p files
cd step2
for i in a*
do
	tr -s "[[:blank:]]" "\n" < $i | grep . > ../files/$i
done
cd ..
