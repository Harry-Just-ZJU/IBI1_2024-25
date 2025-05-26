
# import re
import re

# input the one	of three possible splice donor/acceptor combinations
combination = input("please provide the combination: ")

# set the input and output path
input = 'Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output = f'Practical7/{combination}_spliced_genes.fa'

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

# find donor and accepter
keys_to_delete = []
for gene_name in genes:
    cut = combination[:2] + r'.*' + combination[2:]
    seqs = re.search(cut, genes[gene_name])
    if  not seqs:
        keys_to_delete.append(gene_name)

for key in keys_to_delete:
    del genes[key]

# repeat 
tata_genes = {}
for gene_name, sequence in genes.items():
    if re.search(r'TATA[AT]A[AT]', sequence):
        tata_genes[gene_name] = sequence

# output the result
with open(output, 'w') as file:
    for gene_name, sequence in tata_genes.items():
        t = re.findall(r'TATA[AT]A[AT]', sequence)
        file.write('>' + gene_name + ' :' + str(len(t)) + '\n')
        file.write(sequence + '\n')