"""
rosalind.info problem 10: CONS

Given: A collection of at most 10 DNA strings of equal length in FASTA format.
Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)
"""

import sys

file_name = sys.argv[1] #input file with test dataset passed as first argument

def calculate_sequence_length(fname):
    """calculate length of first sequence in file, where sequence is
    split among multiple lines"""
    length = 0
    with open(file_name, "r") as f:
        line = f.readline().strip()
        while line:
            if line[0] != ">":
                length += len(line)
            elif line[0] == ">" and length != 0:
                break
            line = f.readline().strip()
    return length

def rosalind10(fname):
    """produce consensus string and profile matrix from sequence in input file"""
    with open(fname, "r") as f:
        seq_len = calculate_sequence_length(fname) #calculate sequence length
        nucs = ["A", "C", "G", "T"]
        p_matrix = {x:[0]*seq_len for x in nucs} #profile matrix dict

        line = f.readline().strip() #read first line, remove "\n"
        idx = 0 #sequence index
        while line:
            if line[0] != ">": #skip header lines
                for i in range(len(line)):
                    p_matrix[line[i]][idx] += 1 #update consensus matrix
                    idx += 1 #update sequence index
            else:
                idx = 0
            line = f.readline().strip() #read next line

    consensus = "" #initialize empty consensus string
    for i in range(seq_len): #this will also be the consensus sequence length
        max_count = -1 #initialize max_count for position i
        symbol = None #store the symbol corresponding to the max_count
        for nuc in p_matrix:
            if p_matrix[nuc][i] > max_count: #update max_count
                max_count = p_matrix[nuc][i]
                symbol = nuc
        consensus += symbol #add most common symbol for position i to consensus

    return consensus, p_matrix

if __name__ == "__main__":
    #print output for rosalind submission
    c_string, matrix = rosalind10(file_name)
    print(c_string)
    for nuc in matrix:
        print(f'{nuc}:', *matrix[nuc])
