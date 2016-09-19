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
    result=()
    result_longest=()
    max_orf_len=0

    while len(seq)>3:
        orf_end_list=[]
        if 'ATG' in seq:
            orf_begin=seq.find('ATG')

            if 'TGA' in seq[orf_begin+3:]:
                orf_end_list.append(seq.find('TGA'))
            if 'TAG' in seq:
                orf_end_list.append(seq.find('TAG'))
            if 'TAA' in seq:
                orf_end_list.append(seq.find('TAA'))

            orf_end_list.sort()
            while len(orf_end_list)!=0:
                if len(seq[orf_begin:orf_end_list[0]+3])%3==0:
                    next_seq_start=orf_end_list[0]+3
                    if len(seq[orf_begin:orf_end_list[0]+3])>max_orf_len:
                        result_longest=seq[orf_begin:orf_end_list[0]+3]
                        max_orf_len=len(result_longest)
                    result+=(seq[orf_begin:orf_end_list.pop(0)+3],)
                    break
                else:
                    orf_end_list.pop(0)
                    next_seq_start=orf_begin+3
            seq=seq[next_seq_start:]
        else:
            break
          #if len(seq[orf_begin:orf])
    return result, result_longest



#b)
print(len(longest_orf(f_string)[1]))

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

#print(len(f_string))
#print(len(longest_orf(f_string))//3)

result=dna_to_protein(longest_orf(f_string)[1])
print(type(result))
print(len(''.join(result)))

with open('aa.txt','w') as f:
    f.write(''.join(result))
#print(str(result))
