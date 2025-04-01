
# import re
import re

# input the one	of three possible splice donor/acceptor combinations
combination = input("please provide the combination: ")

# set the input and output path
input = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output = f'{combination}._spliced_genes.fa'

# repeat the last problem
genes = {}
with open(input, 'r') as file:
    for line in file:
        line = line.strip()
        if re.search(r'^>', line):
            gene_name = re.findall(r'gene:(\S+)', line)
            genes[gene_name[0]] = ''
        else:
            genes[gene_name[0]] += line

# cut off
for gene_name in genes:
    cut = combination[:2] + r'.*' + combination[2:]
    seqs = re.findall(cut, genes[gene_name])
    if seqs:
        for seq in seqs:
            genes[gene_name] = re.sub(seq, '', genes[gene_name])

# repeat 
tata_genes = {}
for gene_name, sequence in genes.items():
    if re.search(r'TATA[AT]A[AT]', sequence):
        tata_genes[gene_name] = sequence

with open(output, 'w') as file:
    for gene_name, sequence in tata_genes.items():
        file.write('>' + gene_name + '\n')
        file.write(sequence + '\n')
