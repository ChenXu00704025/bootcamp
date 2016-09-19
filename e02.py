#
#----------Exercise 2.2-------------------------------
import os
import bioinfo_dicts

with open('data/salmonella_spi1_region.fna','r') as f:

    # read into a list
    f.seek(0)
    f_list=f.readlines()

    # get rid of the first line
    f_list2=f_list[1:]

    # initialize the sequence string
    f_string=''

    # strip the newline '\n' from the end of each string
    # append to f_string
    for i,string in enumerate(f_list2):
        f_string+=str(f_list2[i].rstrip())

    #print(f_string[0])
    with open('f_string.txt','w') as f:
        f.write(f_string)
    f.close()

with open('f_string_2.txt','r') as f2:
        fstring=f2.read()
        print(len(fstring))

#----------Exercise 2.3-------------------------------
'''
#a)
def gc_blocks(seq,block_size):

    # determine # of blocks
    block_num=len(seq)//block_size

    # initialize result to be returned
    gc_content=()

    # iterate blocks
    for i in range(block_num):

        # initilize count within every block
        count=0

        # iterate every base within a block_size
        for base in seq[i*block_size:(i+1)*block_size]:
            if base in 'GCgc':
                count+=1
        gc_content+=(count/block_size,)

    return gc_content

# b)
def gc_map(seq,block_size,gc_thresh):
    # determine # of blocks
    block_num=len(seq)//block_size

    # initialize the new map
    new_seq=''

    # Bonus function: return tuple with patho information
    patho_seq=()

    # iterate blocks
    for i in range(block_num):
        temp=gc_blocks(seq,block_size)
        if gc_blocks(seq,block_size)[i]>gc_thresh:
            new_seq+=seq[i*block_size:(i+1)*block_size].upper()
        else:
            new_seq+=seq[i*block_size:(i+1)*block_size].lower()
            patho_seq+=(gc_blocks(seq,block_size)[i],seq[i*block_size:(i+1)*block_size].lower())


    return new_seq, patho_seq

# c)
#print(gc_blocks(f_string,1000)[0])
#print(gc_map(f_string, 1000, 0.45)[1])


# d)

mapped_seq=gc_map(f_string,1000,0.45)[0]
formatted_seq=''
for num in range(1,len(mapped_seq)//60):
    formatted_seq+=mapped_seq[(num-1)*60:num*60]+'\n'


#if os.path.isfile('try.txt'):
#    raise RuntimeError('File newFASTA.txt already exists.')

with open('try.txt','w') as f:
    f.write(formatted_seq)

'''
#----------Exercise 2.4-------------------------------
#a)
def longest_orf(seq):
    result=''
    fresult=''
    start_ind=seq.find('ATG')

    # reverse the seq, find the stop criteria indices
    pseudo_end_ind_list=()
    if 'AGT' in seq[::-1]:
        pseudo_end_ind_list+=(seq[::-1].find('AGT'),)
    if 'GAT' in seq[::-1]:
        pseudo_end_ind_list+=(seq[::-1].find('GAT'),)
    if 'AAT' in seq[::-1]:
        pseudo_end_ind_list+=(seq[::-1].find('AAT'),)

    # find the stop criteria index furthest to the right
    pseudo_end_ind=min(pseudo_end_ind_list)

    # convert to the index when the seq isn't reversed
    end_ind=len(seq)-pseudo_end_ind
    result=seq[start_ind:end_ind]
    print(seq[end_ind-3:end_ind])
    print(seq[-3:])
    if len(result)%3==0:
        print(start_ind)
        print(end_ind)
        print(result[-3:])
        fresult=result
    else:
        print('yay')
        longest_orf(result)
    return fresult

#b)
len(longest_orf(f_string))

#c)
#print(bioinfo_dicts.codons)
def dna_to_protein(seq):
    aa=[]
    i=0
    while i<len(seq)//3:
        aa+=bioinfo_dicts.codons[seq[i*3:(i+1)*3]]
        i+=1
    return aa

#print(dna_to_protein(f_string))

#d)
'''
print(len(f_string))
print(len(longest_orf(f_string))//3)

result=dna_to_protein(longest_orf(f_string))
print(type(result))
print(len(''.join(result)))

with open('aa.txt','w') as f:
    f.write(''.join(result))
#print(str(result))
'''
