import sys

file_name = sys.argv[1] #file name is passed as first argument

with open(file_name, "r") as f:
    str1 = f.readline().strip() #read first line
    str2 = f.readline().strip() #read second line

def rosalind6(s1, s2):
    """return hamming distance between two strings, s1 and s2, of equal length.
    Hamming distance corresponds to the number of corresponding symbols that
    differ between the strings"""
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist

if __name__ == "__main__":
    if len(str1) == len(str2):
        print(rosalind6(str1, str2))
    else:
        print("strings must be the same length")
