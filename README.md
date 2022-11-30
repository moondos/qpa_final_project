# Quantori Python Academy Final Project - The genetic code
This is the final project of Quantori Python Academy. The purpose of the project is to help with genetic code investigation. It was build incrementally, using **Python**, **PostgreSQL**, **SQLAlchemy**, **Matplotlib**, **Unittest** & **Docker** and solving 5 different sub-tasks:

1. Building a script for DNA to RNA and RNA to Protein sequence translation. 
2. Сreate a database with four tables that will store this data: dna_bases, rna_bases, codons, polypeptides.
3. Write a function that plots G-C ratio of DNA and saves the resulting graph to a .png or .jpeg file.
4. Pack the project to Docker container with possibility to run the app with command-line arguments.
5. Prepare unit tests for testing the functions from Sub-tasks 1 and 3. 

## Content
***project/script.py***
* A script with two conversion functions inside: convert_dna_to_rna and convert_rna_to_protein that model translation processes. These functions must have a string sequence as input and output.
    - DNA -> RNA input output example: `GTTGTAATGGCCTACATTA` -> `GUUGUAAUGGCCUACAUUA`
    - RNA -> protein input and output example: `GUUGUAAUGGCCUACAUUA` -> `VVMAYI`
* Additionally, script has 2 functions for G-C ratio plot. 
    - The horizontal axis of this graph should be the genome position. The vertical axis should be the G-C ratio in the window. Let the default size of a window be 100 bases.
    - The function must take parameters:
        string: genomic data as a string
        step: int parameter, denoting a width of a bin with a default value of 100 characters.

***project/test_script.py***
* This is a testing script, evaluating the functions from Sub-tasks 1 and 3.

***project/data***
* For the functions in script.py to work, there is a need of data describing how DNA and RNA bases correspond, and same for RNA <-> protein conversion. This data is taken from PostgreSQL database, which is build using `models.py`, `crud.py`, `retrieving.py`.

    > Table dna_bases contains four bases that form a DNA sequence: A, C, G, and T. Table rna_bases contains bases that form an RNA sequence and should be connected to the first table with one-to-one relation. Link the polypeptide table to codons in a one-to-many relation.
* *input* folder contains sample FASTA files which can be used to run the project
    - `genomic.fna` - COVID genom 
    - `dna_sequence.fasts` - Short part of Cow genom

***project/legacy***
* This folder is used for old files.
* data.py - file with codon <-> polypeptide map used for translation without PostgeSQL database

***project/output_data***
* For outputs such as:
    - GC-distribution plot (png file)
    - Protein sequence (txt file)

## How to Run the Project in Docker
1. Copy your FASTA file to data/input folder or use one which is already there
2. Run `docker compose up -d --build`
3. Docker will build Container pack with posgresql and qpafinalproject containers
4. Postgresql container will be running but qpafinalproject will stop after script.py execution. You will see results of the default DNA sequence translation and GC-content plot in the volume *script_data*
5. To run the script:
    - If you want to pass a file to the script, enter below command to the terminal:
        - Run: `docker compose run -it --rm qpafinalproject data/input/genomic.fna 100`
            - data/input/genomic.fna - is a file *path*, positional argument
            - 100 - *step* is width of a bin, optional argument, 100 by default 
    - In case of short dna sequence and step:  
        - uncomment required lines in the `script.py`
            ```python
            parser.add_argument('dna', metavar='dna', type=list, nargs='?', help='Enter DNA sequence', default="ATTTGGCTACTAACAATCTA")
            dna = args.dna
            gc_content_lst = gc_content_subseq(dna, step)
            rna = convert_dna_to_rna(seq)
            protein = convert_rna_to_protein(rna)
            print(protein)
            ``` 
        - comment 
            ```python
            parser.add_argument('path', metavar='path', type=str, nargs='?', help='Enter input file', default="data/input/dna_sequence.fasta")
            covid_genom = SeqIO.read(path, "fasta")
            seq = list(covid_genom)
            gc_content_lst = gc_content_subseq(seq, step)
            rna = convert_dna_to_rna(seq)
            protein = convert_rna_to_protein(rna)
            print(protein)
            ```
        - Run: `docker-compose run --rm  qpafinalproject {dna} {step}`

    > dna is genomic data (ATTTGGCTACTAACAATCTA) as a string and step (3) is denoting a width of a bin
    - If you want to run container continiously through bash:
        - uncomment required line in docker-compose.yml:
        ```entrypoint: ["bash"]```
        - Run:
        `docker compose run -it --rm qpafinalproject`
        - Write a bash command:
        `python script.py data/input/genomic.fna 100`
        
    > In this case container will not stop and you can run the script multiple times without container restart
6. GC-distribution plot (.png) and Protein sequence (.txt) will be in the volume ***script_data*** 
7. To stop and remove all the containers run: `docker-compose down --remove-orphans`

## How to Run the Project without Docker
Everything can be executed from `script.py` file, it contains function calls for translation, database creation and plotting.
> Make sure you amended `crud.py` file to be able to connect to localhost.

```python
'''To run script without docker, replace:
db - localhost
5432 - 5433
'''
engine = create_engine('postgresql+psycopg2://postgres:password@db:5432/project')
```