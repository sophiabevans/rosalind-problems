import sys

file_name = sys.argv[1]

def rosalind3(fname):
    """return reverse complement of dna sequence in text file fname"""
    dna_seq = ""
    #nucleotide complements
    complements = {"A":"T", "T":"A", "C":"G", "G":"C"}

    #read rosalind data file and process contents as a single string dna_seq
    with open(fname, "r") as f:
        line = f.readline()
        while line:
            dna_seq += line.strip().upper()
            line = f.readline()

    #empty string to hold reverse complement of dna_seq
    rev_comp = ""

    #index into dna_seq in reverse order
    for i in range(len(dna_seq) - 1, -1, -1):
        #add complement of each nucleotide to rev_comp string
        rev_comp += complements[dna_seq[i]]
    return rev_comp

if __name__ == "__main__":
    print(rosalind3(file_name))
