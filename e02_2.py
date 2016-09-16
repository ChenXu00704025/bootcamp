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
    result1=()
    result2=()
    longest=0
    while len(seq)>3:
        end_codon_ind_tuple=()
        if 'TGA' in seq:
            end_codon_ind_tuple+=(seq.find('TGA'),)
        if 'TAG' in seq:
            end_codon_ind_tuple+=(seq.find('TAG'),)
        if 'TAA' in seq:
            end_codon_ind_tuple+=(seq.find('TAA'),)
        print(end_codon_ind_tuple)
        if len(end_codon_ind_tuple)==0:
            break

        if 'ATG' in seq[:min(end_codon_ind_tuple)]:
            ATG_ind=seq.find('ATG')
            print('a')
            if len(seq[ATG_ind:min(end_codon_ind_tuple)])%3==0:
                result1+=(seq[ATG_ind:min(end_codon_ind_tuple)+3],)
                if len(seq[ATG_ind:min(end_codon_ind_tuple)+3])>longest:
                    result2=seq[ATG_ind:min(end_codon_ind_tuple)+3]
                    longest=len(seq[ATG_ind:min(end_codon_ind_tuple)+3])
                seq=seq[1:]
                print('b')
                #print(ATG_ind,min(TGA_ind,TAG_ind,TAA_ind))
                #print(result)
            else:
                seq=seq[1:]
                print('c')
        else:
            seq=seq[1:]
            print('d')
            #print(len(seq))
        print(seq)
    return result1,result2

print(longest_orf('GGATGATGATGTAAAAC')[1])

#b)
'''
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
'''
