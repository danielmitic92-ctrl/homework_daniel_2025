def read_file_into_lines(file_path):
    """"
    read file and remove the character at the end
    """
    lines=[]
    with open (file_path,"r") as infile:
      for line in infile.readlines():
          cleaned=line.rstrip()
          lines.append(cleaned)
    return lines


def load_codon_table():
    codon_aa_table =  {"UUU": "F","CUU": "L", "AUU": "I","GUU":"V",
    "UUC": "F",      "CUC": "L", "AUC": "I",      "GUC":"V",
    "UUA": "L",      "CUA": "L", "AUA": "I",      "GUA":"V",
    "UUG": "L",      "CUG": "L", "AUG": "M",      "GUG":"V",
    "UCU": "S",      "CCU": "P", "ACU": "T",      "GCU":"A",
    "UCC": "S",      "CCC": "P", "ACC": "T",      "GCC":"A",
    "UCA": "S",      "CCA": "P", "ACA": "T",      "GCA":"A",
    "UCG": "S",      "CCG": "P", "ACG": "T",      "GCG":"A",
    "UAU": "Y",      "CAU": "H", "AAU": "N",      "GAU":"D",
    "UAC": "Y",      "CAC": "H", "AAC": "N",      "GAC":"D",
    "UAA": "",   "CAA": "Q", "AAA": "K",      "GAA":"E",
    "UAG": "",   "CAG": "Q", "AAG": "K",      "GAG":"E",
    "UGU": "C",      "CGU": "R", "AGU": "S",      "GGU":"G",
    "UGC": "C",      "CGC": "R", "AGC": "S",      "GGC":"G",
    "UGA": "",   "CGA": "R", "AGA": "R",      "GGA":"G",
    "UGG": "W",      "CGG": "R", "AGG": "R",      "GGG":"G"}
    return codon_aa_table

def translate_protein(rna,codon_table):
    "returns string of aminoacids based on string of rna"
    peptide=""
    counter=0
    for base in rna:
        triplet=rna[counter:counter+3]
        if triplet!="" :
            counter=counter+3
            aa=codon_table[triplet]
            peptide=peptide+aa
    return peptide

def motif_locations(sequence,motif):
    "returns list of positions of a motiv in a given sequence"
    motif_locations=[]
    for i in range(len(sequence)):
        current_motif=sequence[i:i+len(motif)]
        if current_motif==motif:
            motif_locations.append(i+1)
    return(motif_locations)

def reverse_complement_rna(rna):
    reverse_complement=""
    for base in rna:
        if base=="A":
            reverse_complement="U"+reverse_complement
        if base=="C":
            reverse_complement="G"+reverse_complement
        if base=="U":
            reverse_complement="A"+reverse_complement
        if base=="G":
            reverse_complement="C"+reverse_complement
    return reverse_complement


def find_start_codons(rf):
    starting_position=[]
    for i in range(0,len(rf),3):
        codon=rf[i:i+3]
        if codon== "AUG":
            starting_position.append(i)
    return(starting_position)


def find_ORF(rf,start,codon_table):
    orf=[]
    for i in range(0,len(rf),3):
        codon=rf[i:i+3]
        if codon_table[codon] == "":
            break
        orf.append(codon)
    return orf
