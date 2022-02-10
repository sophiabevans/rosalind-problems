nucs = ["A", "C", "G", "T"]
counts = {n:0 for n in nucs}

with open("rosalind_dna.txt") as f:
    line = f.readline()
    while line:
        string = line.strip()
        for s in string.upper():
            counts[s] += 1
        line = f.readline()
print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')
