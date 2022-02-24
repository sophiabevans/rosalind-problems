import pickle

def create_rna_codon_dict(filename):
	"""return mapping of codons to amino acids in rna-codon-table file from
	rosalind.info as a dictionary"""
	mRNA_AA_map = {} #initialize empty dictionary

	with open(filename, "r") as f:
		#downloaded from rosalind.info
		#codons are mapped to amino acids with a space between codon and matching aa
		#indeterminate whitespace separates codon aa pairs on each line
		line = f.readline()
		while line:
			l = line.strip().split() #split codons and aa symbols
			for i in range(0, len(l), 2): #i = codon, i + i = aa
				mRNA_AA_map[l[i]] = l[i+1] #ad codon key to dict with aa value
			line = f.readline() #read next line
	return mRNA_AA_map #return dict

def write_dict(filename):
	"""write dictionary to pickle file with name filename"""
	with open(filename, "wb") as f:
		rna_dict = create_rna_codon_dict('rna-codon-table')
		pickle.dump(rna_dict, f)

if __name__ == '__main__':
	#write dictionary as pickle file into helper_files folder
	write_dict("../helper_files/rna-codon-dict.pickle")
