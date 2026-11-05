\# Linux Command-Line Practice for Bioinformatics



\## Project Overview

This repository documents Linux commands practiced during my bioinformatics internship, including file management, FASTA sequence handling, and BLAST result analysis.



\## 1. Directory Navigation



```bash

pwd

ls

cd ..

cd \~

```



\- `pwd` — Display current working directory

\- `ls` — List files and directories

\- `cd ..` — Move to parent directory

\- `cd \~` — Move to home directory



\## 2. File Listing and Inspection



```bash

ls -ltr

ls -ltrh

ls -lh

less query.fasta

```



\- `ls -ltr` — List files by modification time

\- `ls -ltrh` — Show file sizes in readable format

\- `ls -lh` — Display file sizes in KB, MB, or GB

\- `less` — View large files page by page



\## 3. File Management



```bash

rm filename

mv project Documents/

```



\- `rm` — Remove a file

\- `mv` — Move or rename a file



\## 4. Downloading and Remote Access



```bash

wget URL

ssh username@server

```



\- `wget` — Download a file from a URL

\- `ssh` — Connect to a remote server securely



\## 5. FASTA Sequence Handling



```bash

head query.fasta

grep ">" query.fasta

```



\- `head` — View the beginning of a FASTA file

\- `grep ">"` — Identify FASTA sequence headers



Extracting the first sequence from a FASTA file:



```bash

awk '/>/{if(n++) exit} {print}' query.fasta > test\_query.fasta

```



\## 6. BLAST Output Analysis



Searching for alignment scores:



```bash

grep "Score =" tblastx\_all\_hsps.txt | head -10

```



Finding alignment identity information:



```bash

grep -A 6 -m 1 "Identities = 373/379" blast\_results.txt

```



Searching preceding lines for a matching alignment:



```bash

grep -B 15 -m 1 "Identities = 373/379" blast\_results.txt

```



\## Learning Outcomes

\- Practiced Linux terminal navigation

\- Managed files and directories

\- Inspected FASTA sequence files

\- Extracted sequences using `awk`

\- Searched BLAST output using `grep`

\- Interpreted BLAST alignment scores, identities, and E-values



\## Author

Suganya K  

B.Tech Bioinformatics

