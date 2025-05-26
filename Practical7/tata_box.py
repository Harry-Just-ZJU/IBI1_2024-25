
# import re
import re

# set input and output path
input = 'Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output = 'Practical7/tata_genes.fa'

# set the variables
genes = {}

# open input as read
with open(input, 'r') as file:
    for line in file:
        # delete the blank
        line = line.strip()
        
        # record the overall gene and sequence separately
        if re.search(r'^>', line):
            # gene
            gene_name = re.findall(r'gene:(\S+)', line)
            genes[gene_name[0]] = ''
        else:
            # sequence
            genes[gene_name[0]] += line

# find the tata sequence and place them in a new dictionary
tata_genes = {}
for gene_name, sequence in genes.items():
    if re.search(r'TATA[AT]A[AT]', sequence):
        tata_genes[gene_name] = sequence

# write the gene and sequence in the output file
with open(output, 'w') as file:
    for gene_name, sequence in tata_genes.items():
        file.write('>' + gene_name + '\n')
        file.write(sequence + '\n')