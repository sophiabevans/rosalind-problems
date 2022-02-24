import sys

file_name = sys.argv[1]

def process_file(fname):
    """process input file, return dictionary with rosalind ids as keys
    and sequences as values"""
    ids_seqs = {}
    last_key = None

    with open(fname, "r") as f:
        line = f.readline()

        while line:
            if line[0] == ">": #add new id to dictionary
                key = line.strip()[1:]
                ids_seqs[key] = ''
                last_key = key
            else: #add sequence associated with the last id
                ids_seqs[key] += line.strip()
            line = f.readline()
    return ids_seqs

def compute_gc(seq_string):
    """compute gc sequence of input string"""
    length = len(seq_string)
    gc = seq_string.count("G") + seq_string.count("C")
    return gc / length #return proportion of sequence that is G or C


def rosalind5(fname):
    """print id and GC content of the string with highest GC content"""
    seq_dict = process_file(fname) #store ids and sequences in a dict
    max_gc = -1
    ros_id = None
    for key in seq_dict:
        gc = compute_gc(seq_dict[key]) #compute gc content
        if gc > max_gc: #save the max gc content and id
            max_gc = gc
            ros_id = key
    print(f'{ros_id}\n{max_gc * 100}') 

if __name__ == "__main__":
    rosalind5(file_name)
