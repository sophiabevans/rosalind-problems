"""
Rosalind Problem 9 SUBS Description:
Given: Two DNA strings s and t
Return: All locations of t as a substring of s
"""
import sys

file_name = sys.argv[1] #input file with test dataset passed as first argument

with open(file_name, "r") as f:
    #first line is full string, second line is substring
    #add upper() to protect against mistakes in comparisons in rosalind9
    string = f.readline().strip().upper()
    substring = f.readline().strip().upper()

def rosalind9(s, t):
    sub_length = len(t) #length of substring
    string_length = len(s) #length of search string
    match_locs = []
    for i in range(string_length - sub_length): #traverse string s
        if s[i] == t[0]: #only do full comparison where beginning matches
            if s[i : i + sub_length] == t:
                match_locs.append(i + 1) #string is 0 indexed but result is not
    return match_locs

if __name__ == "__main__":
    print(*(rosalind9(string, substring)))
