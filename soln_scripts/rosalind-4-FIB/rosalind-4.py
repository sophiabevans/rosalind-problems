import sys

file_name = sys.argv[1] #test dataset file name passed as first argument

with open(file_name, "r") as f:
    line = f.readline()
    n, k = line.strip().split()

months = int(n)
litter_size = int(k)

def rosalind4(months, litter_size):
    rabbits = [1, 1] #F0 = F1 = 1
    i = 1 #index variable
    while len(rabbits) < months:
        #offspring = rabbits alive months ago * k, add new rabbits
        rabbits.append((rabbits[i-1] * litter_size) + rabbits[i])
        i += 1 #increment index
    return rabbits[-1]

if __name__ == "__main__":
    print(rosalind4(months, litter_size))
