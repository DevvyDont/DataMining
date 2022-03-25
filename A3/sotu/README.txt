Files in the "sotu/" directory
  - files/       - individual speeches
      + a1.txt
      + a2.txt
      + ...
      + a231.txt
  - party.txt - a file containing the party information for each president
  - preprocess.sh - the top-level shell script used to preprocess the data
  - README.txt - this document
  - source-information.txt - information on where the original data was collected and other sources of information on the data set
  - stateoftheunion1790-2017.txt - the original data set
  - stopwords.txt - a file listing stopwords to be removed when preforming the analysis


This original data file was processed into the 231 individual text files you will use in the "files/" directory. 
Each file "a1.txt", "a2.txt", ..., "a228.txt" represents a speech starting from George Washington ending with President Obama's speech in 2014. 

The transcript of the speech was processed to remove punctuation, remove numbers, and convert the characters all to lowercase.  The files are structured to have one word per line listed.   The preprocessing was completed using the script "preprocess.sh".

The text files are what you will use in your project.

