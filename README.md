#Introduction

This assignment is a part of the course INST767 - Big Data Infrastructure at University of Maryland.
Following is the instruction for the assingment:

1. Find the bi-gram frequencies from a collection of documents.

2. Find the average of a large collection of numbers. You can imagine that the input files will only contain numbers; one number per line. There can be multiple files.

##Part 1
Part 1 folder contains mapper and reducer files for the first part of the assignment to calculate bi-gram frequencies.
The assumption made for this assignment is that the sentences in the files in each line will not have punctuation. Also, the cases are being considered and hence `Alpha` and `alpha` will be considered as different words.

#Part 2
Part 2 folder contains mapper and reducer files for the second part of the assignment to calculate the average of large collection of numbers.
Assumption is as per the instruction that only one number is present in one line.