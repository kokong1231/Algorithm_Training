from operator import itemgetter

book = {'A' : 'AA', 'B' : 'AD', 'C' : 'AF', 'D' : 'AG', 'E' : 'AV', 'F' : 'AX',\
        'G' : 'DA', 'H' : 'DD', 'I' : 'DF', 'J' : 'DG', 'K' : 'DV', 'L' : 'DX',\
        'M' : 'FA', 'N' : 'FD', 'O' : 'FF', 'P' : 'FG', 'Q' : 'FV', 'R' : 'FX',\
        'S' : 'GA', 'T' : 'GD', 'U' : 'GF', 'V' : 'GG', 'W' : 'GV', 'X' : 'GX',\
        'Y' : 'VA', 'Z' : 'VD', '0' : 'VF', '1' : 'VG', '2' : 'VV', '3' : 'VX',\
        '4' : 'XA', '5' : 'XD', '6' : 'XF', '7' : 'XG', '8' : 'XV', '9' : 'XX',\
        ' ' : 'AC'}

text = input('문자열을 입력하세요 : ')
key_text = input('암구어를 입력하세요 : ')
key_list = list(key_text)

def re_book(book_value):
    
    rev_book = {}
    for x in book_value:
        re = book_value[x]
        rev_book[re] = x

    return rev_book
    
def changer(text, book):                  #환자 암호로 전환

    change = []
    
    for x in text:
        val = book[x]
        change.append(val)

    return change

def rm_sort(key):                         #암구어 문자 중복 제거
    my_set = set()
    save = []

    for e in key:
        if e not in my_set:
            save.append(e)
            my_set.add(e)

    return save

def list_creat(key_top,text_list_value,len_text,len_key):

    save_text = [['P']*2 for i in range(len_key)]
    
    for x in range(int(len_key)):
        if save_text[x][0] == ('P'):
            save_text[x][0] = key_top[x]
    
    for y in range(int(len_text)):
        if save_text[y%len_key][1] == ('P'):
            save_text[y][1] = text_list_value[y]
            
        else:
            save_text[y%len_key].append(text_list_value[y])
            
    for z in range(int(len_key)):
        if len(save_text[z]) != len(save_text[(z+1)%len_key]):
            save_text[z+1].append('P')
        
    return save_text

def sort_print(temp,key_num,new_temp):
    temp.sort(key = itemgetter(0))
    
    print_enc = []
    
    for x in range(key_num):
        new_temp[x].pop(0)
    
    for y in new_temp:
        for z in y:
            print_enc.append(z)
    
    return print_enc

def relist(list_value, key_value, count, table_value):

    save_list = []
    save_list_o = [[]*1 for i in range(len(key_value))]
    save_list_x = []
    num = 0
    pop_data = []
    
    for x in key_value:
        for y in range(len(key_value)):
            if list_value[y][0] == x:
                save_list.append(list_value[y])
    
    for t in range(len(key_value)):
        l = save_list[t].pop(0)
        pop_data.append(l)
    
    for r in range(int(count / len(key_value))):
        for o in save_list:
            pop_x = o.pop(0)
            save_list_x.append(pop_x)
    
    for o in range(count):
        if len(save_list_o[num]) >= int(count/len(key_value)):
            num = num + 1
        
        save_list_o[num].append(save_list_x[o])
    
    for k in range(len(key_value)):
        save_list_o[k].insert(0, pop_data[k])
    
    for z in range(count + len(key_value)):
        if save_list_o[z%len(key_value)].count('P') >= 1:
            if save_list_o[z%len(key_value)].index('P') >= 1:
            
                check = save_list_o[z%len(key_value)].pop(save_list_o[z%len(key_value)].index('P'))
            
                del check
    
    return save_list_o

def creat_enc_list(enc_value,key_value,len_text,len_key):

    save_text = [[]*1 for i in range(len_key)]

    for x in range(int(len_key)):
        if len(save_text[x]) <= 1:
            save_text[x].append(key_value[x])
    
    for y in range(int(len_text)):
        save_pop = enc_value.pop(0)
        
        if len(save_text[int(y/int(len_text/len_key))])  <= int(len_text/len_key):
            save_text[int(y/int(len_text/len_key))].append(save_pop)
            
        else:
            save_text[int(y/len_key) + 1].append(save_pop)
    
    return save_text

def creat_decbook_list(dec_text_value,len_text,len_key):

    decbook = [[]*1 for i in range(int(len_text/2))]
    sum_decbook = []
    
    for x in range(len_text):
        if len(decbook[int(x/2)]) < 2:
            decbook[int(x/2)].append(dec_text_value[x])
        
    for y in range(int(len_text/2)):
        sum_dec = "".join(decbook[y])
        sum_decbook.append(sum_dec)
    
    return sum_decbook

sum_text = "".join(changer(text, book))
sum_text_list = list(sum_text)

len_text_o = len(sum_text_list)
len_key = len(rm_sort(key_list))

key_list_value = rm_sort(key_list)
key_list_sort = sorted(key_list_value)

save_list_creat = list_creat(key_list_value, sum_text_list,len_text_o,len_key)
enc_text = sort_print(save_list_creat, len_key, save_list_creat)
print('\n암호문 : ', "".join(enc_text))

len_text_enc = len(enc_text)

new_book = re_book(book)

enc_list_make = creat_enc_list(enc_text,key_list_sort,len_text_enc,len_key)

relist_value = relist(enc_list_make, key_list_value, len_text_enc, len(sum_text_list))
dec_text = sort_print(save_list_creat, len_key, relist_value)
dec_change_text = creat_decbook_list(dec_text, len(dec_text), len(key_list))
dec_value = changer(dec_change_text, new_book)
print('\n복호문 : ', "".join(dec_value))
