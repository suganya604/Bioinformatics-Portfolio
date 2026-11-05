\# BLAST Sequence Analysis



\## Project Overview

This project documents my hands-on learning of BLAST (Basic Local Alignment Search Tool) using the Linux command line.



\## Objective

To understand sequence similarity, alignment, and biological sequence comparison using BLAST.



\## Tools Used

\- BLAST+

\- Linux terminal

\- FASTA format

\- Git and GitHub



\## BLAST Programs



\### 1. BLASTN

BLASTN compares a nucleotide query sequence against a nucleotide database.



\### 2. TBLASTX

TBLASTX translates nucleotide sequences in all six reading frames and compares the translated protein sequences.



\## Important Concepts



| Term | Explanation |

|---|---|

| Query | The sequence submitted for searching |

| Database | Collection of sequences used for comparison |

| Alignment | Arrangement of sequences to identify similarities |

| Identity | Percentage of identical residues in an alignment |

| Bit Score | Measures alignment strength |

| E-value | Estimates chance of obtaining an alignment of similar quality |

| Gaps | Insertions or deletions in an alignment |



\## Commands Practiced



```bash

blastn -query query.fasta -db mydb.fasta -out blast\_results.txt

```



```bash

tblastx -query query.fasta -subject mydb.fasta -out tblastx\_results.txt

```



```bash

grep "Score =" tblastx\_results.txt

```



\## Result Interpretation

\- Higher bit score generally indicates a stronger alignment.

\- Lower E-value indicates a more statistically significant match.

\- Higher percentage identity indicates more identical aligned residues.



\## Learning Outcomes

\- Understanding FASTA sequence files

\- Running BLAST from the Linux terminal

\- Comparing nucleotide sequences

\- Interpreting alignment results

\- Practicing command-line bioinformatics



\## Data Privacy

This repository contains learning documentation only. Confidential internship datasets are not uploaded.



\## Author

Suganya K  

B.Tech Bioinformatics



