def makeCodebook():
    decbook = {'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h',\
               '6':'i','0':'l','9':'m','*':'n','%':'o','=':'p','(':'r',')':'s',\
               ';':'t','?':'u','@':'v',':':'y','7':' '}

    encbook = {}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k

    return encbook, decbook

def encrypt(msg, encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])

    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c,decbook[c])

    return msg

def move(text):                     # 전치 암호 구현
    a = int(len(text) / 2)          # 환자 암호의 길이를 절반으로 나눈 값을 저장
    b = list(text)                  # 환자암호를 배열로 만듬

    for x in range(a):              # 환자암호의 맨앞을 꺼내고 맨뒤로 보내는작업
        c = b.pop(0)
        b.append(c)

    return b

def remove(text):                    #전치 암호 복호화
    a = (int(len(text) / 2)-1)          
    b = list(text)                  

    for x in range(a + 1):          
        c = b.pop(0)
        b.append(c)

    return b

if __name__== '__main__' :
    plaintext = 'I love you with all my heart'

    encbook, decbook = makeCodebook()
    ciphertext = encrypt(plaintext, encbook)    #환자 암호
    print(ciphertext)

    move_text = move(ciphertext)                #전치 암호 호출
    
    o = "".join(move_text)                      #배열을 문자열로 전환
    print(o)

    move = remove(o)
    c = "".join(move)

    deciphertext = decrypt(c, decbook)
    print(deciphertext)
