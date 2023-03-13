AMINOACIDS = {
    ("AUG"): "Methionine",
    ("UUU", "UUC"):"Phenylalanine",
    ("UUA", "UUG"): "Leucine",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("UAU", "UAC"): "Tyrosine",
    ("UGU", "UGC"): "Cysteine",
    ("UGG"): "Tryptophan",
}

def get_codons(strand):
    return [strand[i:i+3] for i in range(0, len(strand), 3)]


def proteins(strand):
    codons = get_codons(strand)
    proteins_list = []
    for codon in codons:
        if codon in ("UAA", "UAG", "UGA"):
            break
        for key in AMINOACIDS:
            if codon in key:
                proteins_list.append(AMINOACIDS[key])
    return proteins_list

