import sys

file_name = sys.argv[1]

def rosalind2(fname):
    dna_seq = ""
    rna_seq = ""

    with open(fname, "r") as f:
        line = f.readline()
        while line:
            dna_seq += line.strip().upper()
            line = f.readline()

    rna_seq = dna_seq.replace("T", "U")
    return rna_seq

if __name__ == "__main__":
    print(rosalind2(file_name))
