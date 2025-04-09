
# 3 Restriction enzyme cut sites

import re 

def find_restriction_site(DNA_seq, restriction_site):

    site = []
    canonical = ['A', 'T', 'G', 'C']
    for nucleotide in DNA_seq:
        if nucleotide not in canonical:
            return 'The DNA sequence should contain only canonical nucleotides.'
        
    for nucleotide in restriction_site:
        if nucleotide not in canonical:
            return 'The restriction enzyme recognition sequence should contain only canonical nucleotides.'
        
    if re.search(restriction_site, DNA_seq):
        for i in range(len(DNA_seq)):
            seq = DNA_seq[i : i + len(restriction_site)]

            if seq == restriction_site:
                site.append(f'position{ i + 1 }')
        return 'Restriction sites are found at '+ ', '.join(site) + '.'

    else:
        return "No restriction site found!"
    
# example
print(find_restriction_site('ATGCGTAATCGCTAACTGCTACGCTA','GCTA'))

DNA = input('please write the DNA sequence: ')
restriction = input('please write the restriction enzyme recognition sequence: ')
print(find_restriction_site(DNA, restriction))