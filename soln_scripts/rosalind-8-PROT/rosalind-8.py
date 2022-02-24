import sys
import pickle #data from rna-codon-table was saved as a dictionary

file_name = sys.argv[1] #first argument holds file name

with open(file_name, "r") as f:
    #read the input mRNA string from file_name, no newline character
    mRNA = f.readline().strip()

with open("../helper_files/rna-codon-dict.pickle", "rb") as f:
    codon_dict = pickle.load(f) #load codon/aa mapping dict from pickle file

def rosalind8(s, codon_map):
    """given an input mRNA string s and mapping of RNA codons to
    amino acid symbols, return the protein string encoded by s"""
    #read codons of length 3
    prot = "" #initialize empty string to hold amino acid sequence
    for i in range(0, len(s), 3):
        codon = s[i: i+3]
        AA = codon_map[codon] #map codon to aa
        if AA == "Stop":
            break #translation terminated
        prot += AA #add aa to protein string
    return prot


if __name__ == "__main__":
    assert not (len(mRNA) % 3) #codons are length 3, should be a multiple of 3
    print(rosalind8(mRNA, codon_dict))
