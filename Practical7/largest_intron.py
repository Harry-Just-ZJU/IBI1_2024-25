
import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron = re.findall(r'GT.+AG', seq)

lens = 0
for introns in intron:
    lens += len(introns)
print(intron)

print(lens)