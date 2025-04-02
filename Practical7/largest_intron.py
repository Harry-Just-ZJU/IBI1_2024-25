
# import re 
import re

# find the sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron = re.findall(r'GT.+AG', seq)

# calculate the length
lens = 0
for introns in intron:
    lens += len(introns)
print(intron)

print(lens)