text = input('문자열을 입력하세요. : ')
text_save = list(text)

key = input('키 값을 입력하세요. : ')

def enc(key_num):
    global text_save
    
    save = []
    
    for x in text_save:
        ord_text = ord(x)

        if int(ord_text) >= 65 and int(ord_text) <= 90:
            enc_changer = (((int(ord_text) + int(key_num)) - 65) % 26) + 65

        if int(ord_text) < 65:
            enc_changer = int(ord_text) + int(key_num)

        if int(ord_text) >= 97 and int(ord_text) <= 122:
            enc_changer = (((int(ord_text) + int(key_num)) - 97) % 26) + 97

        else:
            enc_changer = int(ord_text) + int(key_num)
        
        chr_text = chr(enc_changer)
        save.append(chr_text)
    
    return save

save_temp = enc(key)

def dec(key_num):
    
    save_ii = []

    for y in save_temp:
        ord_text = ord(y)

        if int(ord_text) >= 65 and int(ord_text) <= 90:
            dec_changer = (((int(ord_text) - int(key_num)) - 65) % 26) + 65

        if int(ord_text) < 65:
            dec_changer = int(ord_text) - int(key_num)

        if int(ord_text) >= 97 and int(ord_text) <= 122:
            dec_changer = (((int(ord_text) - int(key_num)) - 97) % 26) + 97

        else:
            dec_changer = int(ord_text) - int(key_num)
                           
        chr_text = chr(dec_changer)
        save_ii.append(chr_text)

    return save_ii

print('\n암호화')
print("".join(enc(key)))
print('\n복호화')
print("".join(dec(key)))
