# compliment base
#import sys
#seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'

def complement_base(base):
    if base == 'A' or base == 'a':
        return 'T'
    elif base == 'T' or base == 't':
        return 'A'
    elif base == 'G' or base =='g':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq):
    rev_seq=''
    for base in reversed(seq):
        rev_seq+=complement_base(base)
    return rev_seq


def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""

    if base == 'A' or base == 'a':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base == 'T' or base == 't' or base == 'U' or base == 'u':
        return 'A'
    elif base == 'G' or base == 'g':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)
    print(rev_seq)
    return rev_seq



#print(reverse_complement(seq,material='RNA'))
