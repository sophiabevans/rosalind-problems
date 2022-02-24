import sys

file_name = sys.argv[1] #path to file as first argument

def rosalind1(fname):
    """count the number of A, C, G, and T nucleotides in the DNA sequence
    in text file fname, return A C G T counts separated by a space """
    nucs = ["A", "C", "G", "T"]
    counts = {n:0 for n in nucs} #initialize dict to hold nucleotide counts

    with open(fname) as f:
        line = f.readline() #read first line
        while line:
            for s in line.strip().upper(): #process line
                counts[s] += 1 #update nucleotide counts
            line = f.readline()
    return(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')

#print rosalind1() output
if __name__ == "__main__":
    print(rosalind1(file_name))
