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
~~~

## Homework 2

Write a small python script that converts FASTA to Leave NEXUS.

Conditions:

    It must take a FASTA file as input
    As an argument
    Or from STDIN
    Every operation must be within a function
    Each function must have its own docstring
    Describe arguments and return value
    NEXUS file is outputted to STDOUT
    Assume "N" and "-" as missing and gap characters respectively
    NEXUS file has a "MrBayes Block" where ngen and outgroup are provided as arguments
    Sequence names must be capped to 99 characters

## Getting Started
Using the written script Homework2.py that converte FASTA to *Leave* NEXUS format.<br>
In Shell:
~~~ Shell script
python homework2_asb.py file.fasta outgroup ngen
~~~
Example:
~~~ Shell script
python homework2_asb.py example.fasta vulgaris 4000
~~~
