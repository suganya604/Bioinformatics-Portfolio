# DNA Sequence Analyzer

sequence = raw_input("Enter a DNA sequence: ")

sequence = sequence.upper()

valid_bases = "ATGC"

if all(base in valid_bases for base in sequence):

    length = len(sequence)

    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    gc_content = ((count_G + count_C) / length) * 100
    at_content = ((count_A + count_T) / length) * 100

    print("\nDNA Sequence Analysis")
    print("---------------------")
    print("Sequence:", sequence)
    print("Length:", length)
    print("A count:", count_A)
    print("T count:", count_T)
    print("G count:", count_G)
    print("C count:", count_C)
    print("GC Content:", round(gc_content, 2), "%")
    print("AT Content:", round(at_content, 2), "%")

else:
    print("Invalid DNA sequence! Use only A, T, G, C.")