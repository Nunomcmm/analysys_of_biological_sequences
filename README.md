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

# Homework 2

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

# Assignment 2

Your Task:

    Figure out if the data has the resolution to distinguish between Pungent and Bland individuals.
    What groups can you identify?
    Write a report on what you did to try to answer that question;
    Keep in mind that your are not analysing a full dataset, but rather a heavily down-sampled subset.

In detail:

    Write an introduction section describing the sequencing method you are working with;
    Highlight the importance of HTS data on being able to perform the task you are resolving;
    Make sure you have a Materials & Methods section where you detail how your analyses were performed;
    Do not forget to describe the dataset as best you can!
    Include a results section where you describe the results you have obtained;
    Interpret the results in a biological context in the Discussion section;
    Optionally, finish with a conclusion section if you think it makes sense in your specific case;

## Getting Started

To run it is necessary to make it executable, using the following code: <br>
~~~ Shell script
chmod +x scriptname
~~~

If you don't have anaconda installed, run Script1 available in Assignment2_Anexos.<br>
~~~ Shell script
bash Script1_Assignment2
~~~

To get analysis from ipyrad, run Script2.<br>
~~~ Shell script
bash Script2_Assignment2
~~~
For building the trees, you need RAxML and MrBayes to perform your run of Script3.<br>

~~~ Shell script
bash Script3_Assignment2
~~~

When doing the analyses of principal components use the following code: <br>

 ~~~ Shell script
 rstudio Cornales.R
 ~~~
