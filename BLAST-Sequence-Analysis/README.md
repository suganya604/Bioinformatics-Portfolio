# BLAST Sequence Analysis

## Project Overview
Hands-on practice of nucleotide sequence similarity analysis using BLAST command-line tools during my bioinformatics internship.

## Objective
To compare query nucleotide sequences against a sequence database and understand local sequence alignment results.

## Dataset
- Query file: `query.fasta`
- Subject/database file: `mydb.fasta`
- Sequence format: FASTA

*Note: Internship data is not uploaded to this public repository.*

## Tools Used
- BLAST+
- Linux terminal
- FASTA format
- Git and GitHub

## BLASTN Analysis
BLASTN compares nucleotide sequences against a nucleotide database.

Command practiced:

```bash
blastn -query query.fasta -db mydb.fasta -out blast_results.txt
```

## TBLASTX Analysis
TBLASTX translates nucleotide sequences in all six reading frames and compares the translated sequences to identify potential similarities at the protein level.

Command practiced:

```bash
tblastx -query query.fasta -subject mydb.fasta -out tblastx_pairwise.txt
```

## Result Interpretation

| Parameter | Meaning |
|---|---|
| Query | Sequence submitted for comparison |
| Subject | Sequence matched against the query |
| Identity | Percentage of identical aligned residues |
| Bit Score | Alignment score; higher generally indicates a stronger match |
| E-value | Expected number of chance matches; lower indicates stronger statistical significance |
| Gaps | Insertions or deletions in the alignment |
| Reading Frame | Frame used to translate nucleotide sequences |

## Example Result
An alignment observed during practice:

- Identities: 373/379 (98%)
- Gaps: 1/379 (0%)
- Bit Score: 665 bits
- E-value: 0.0

This alignment showed high sequence identity. The E-value of 0.0 indicates that the expected chance occurrence was extremely small, below the program's displayed precision.

## Learning Outcomes
- Executed BLAST commands in a Linux terminal
- Compared nucleotide sequences
- Practiced BLASTN and TBLASTX
- Interpreted sequence identity, bit score, E-value, gaps, and reading frames

## Author
Suganya K  
B.Tech Bioinformatics