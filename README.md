# Quantori Python Academy Final Project - The genetic code
This is the final project of Quantori Python Academy. The purpose of the project is to help with genetic code investigation. It was build incrementally, using Python, PostgreSQL, SQLAlchemy & Matplotlib and solving 5 different sub-tasks.

1. Building a script for DNA to RNA and RNA to Protein sequence translation. 
2. Сreate a database with four tables that will store this data: dna_bases, rna_bases, codons, polypeptides.
3. Write a function that plots G-C ratio of DNA and saves the resulting graph to a .png or .jpeg file.

# Content
project/script.py
* A script with two conversion functions inside: convert_dna_to_rna and convert_rna_to_protein that model translation processes. These functions must have a string sequence as input and output.
* Also, functions for G-C ration plot. The horizontal axis of this graph should be the genome position. The vertical axis should be the G-C ratio in the window. Let the default size of a window be 100 bases.
The function must take parameters:
string: genomic data as a string,
step: int parameter, denoting a width of a bin with a default value of 100 characters.

project/data
* For the functions in script.py to work, there is a need of data describing how DNA and RNA bases correspond, and same for RNA <-> protein conversion. This data is taken from PostgreSQL database, which is build using models.py, crud.py.
* Table dna_bases contains four bases that form a DNA sequence: A, C, G, and T. Table rna_bases contains bases that form an RNA sequence and should be connected to the first table with one-to-one relation. Link the polypeptide table to codons in a one-to-many relation.

project/legacy folder is used for old files.
* data.py - file with codon <-> polypeptide map used for translation on the first task

# How to Run the Project
Everything can be executed from script.py file, it contains function calls for translation, database creation and plotting.

# How to Run the Project in Docker

1. Run docker compose up --build
2. Docker will build Container pack with posgresql and qpafinalproject containers
3. Postgresql container will be running but qpafinalproject will stop after script.py execution. You will see results of the default DNA sequence translation in command line and GC-content plot in the volume
4. To run the script with commandline arguments open a new terminal and enter: 
    docker-compose run --rm  qpafinalproject {dna} {step}
    where dna is genomic data (str) as a string and step (int) is denoting a width of a bin
5. To stop and remove all the container run: docker-compose down --remove-orphans





