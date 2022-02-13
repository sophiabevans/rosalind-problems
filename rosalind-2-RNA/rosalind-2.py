import sys

file_name = sys.argv[1] #path to file with dna sequence

def rosalind2(fname):
    """convert dna sequence in file fname to rna sequence by changing Ts to Us"""

    dna_seq = ""
    rna_seq = ""

    #read dna sequence from input file and save as a single string
    with open(fname, "r") as f:
        line = f.readline()
        while line:
            dna_seq += line.strip().upper()
            line = f.readline()

    #replace T with U to convert dna sequence to rna sequence
    rna_seq = dna_seq.replace("T", "U")
    return rna_seq

#print rosalind2() output
if __name__ == "__main__":
    print(rosalind2(file_name))
