# What is this?
This repository is for save all homeworks of course unit "Analysis of Biological Sequences".

# Homework 1
Write a small script to retrieve sequences that:

    ­Uses the Entrez API
    Allows the user to choose which database to query
    ­Allows the user to pass a search term
    ­Takes user input as command line arguments
    ­Uses the "history" API feature
    ­The result has to be in FASTA format and sent to STDOUT

## Getting Started
Using the written script homework1_asb.py to retrieve sequences in FASTA format.<br>
In Shell:
~~~ Shell script
python homework1_asb.py database term retmax
~~~
Example:
~~~ Shell script
python homework1_asb.py nucleotide "castella castella" 40
