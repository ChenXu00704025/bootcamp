# Python bootcamp Day2
import numpy as np
import compliment_base
import bioinfo_dicts as bd
'''
print(np.mean([1, 2, 3, 4, 5]))
print(np.mean((4.5, 1.2, -1.6, 9.0)))

import sys
seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'

my_dict={'a':6,'b':7,'c':27.6}
print(my_dict)
'''
# The set of DNA bases
bases = ['T', 'C', 'A', 'G']

# Build list of codons
codon_list = []
for first_base in bases:
    for second_base in bases:
        for third_base in bases:
            codon_list += [first_base + second_base + third_base]

# The amino acids that are coded for (* = STOP codon)
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'

# Build dictionary from tuple of 2-tuples (technically an iterator, but it works)
codons = dict(zip(codon_list, amino_acids))

# Show that we did it

#print(codons)
print(bd.aa)
