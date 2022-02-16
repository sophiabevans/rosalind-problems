import sys
from math import comb

file_name = sys.argv[1] #file name is passed as first argument

def rosalind7(fname):
    """
    Description from rosalind.info:

    Given: Three positive integers k, m, and n, representing a population
    containing k+m+n organisms:
    k individuals are homozygous dominant for a factor,
    m are heterozygous, and n are homozygous recessive.

    Return: The probability that two randomly selected mating organisms will
    produce an individual possessing a dominant allele (and thus displaying
    the dominant phenotype). Assume that any two organisms can mate.
    """

    #read in k, m, and n from the dataset file
    with open(fname, "r") as f:
        line = f.readline() #read line
        #unpack values as ints into k, m, n
        k, m, n = map(int, line.strip().split(" "))

    pop_size = k + m + n #total mating organisms in population

    #total possible pairs of mates = combinations of size 2
    total_pairs = comb(pop_size, 2)

    #there are n choose 2 pairs of homozygous recessive mates
    pair_n = comb(n, 2)

    #there are m choose 2 pairs of heterozygous mates
    pair_m = comb(m, 2)

    #there are (m + n choose 2 - pair_n - pair_m) hom rec ~ het mate pairings
    pair_mn = comb(m + n, 2) - pair_n - pair_m

    #of pair_m, 1/4 of het ~ het offspring lack a dom allele
        #(Aa x Aa = (AA, Aa, Aa, aa))
    # of pair_mn, 1/2 of het ~ hom rec offspring lack a dom allele
        #(Aa x aa = (Aa, Aa, aa, aa))
    no_dom = pair_n + (pair_m / 4) + (pair_mn / 2)

    #total matings that produce a dominant allele
    has_dom = total_pairs - no_dom

    #return proportion of possible matings whose offspring have a dom allele
    return has_dom/total_pairs


if __name__ == "__main__":
    print(rosalind7(file_name))
