string='aabcdsdssssssssd'
list_string=list(string)
cur_index=fin_index=0
table={}
length=len(list_string)

while cur_index<length:
    if list_string[cur_index] not in table:
        table[list_string[cur_index]]=1
        list_string[fin_index]=list_string[cur_index]
        fin_index+=1
    cur_index+=1
print(''.join(x for x in list_string[:fin_index]))
