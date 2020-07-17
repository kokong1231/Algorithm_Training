def frequency_analysis(msg):

    fa = {}
    for c in msg:
        if c in fa:

            fa[c] += 1

        else:

            fa[c] = 1

    print(sorted(fa.items(), key=lambda x:x[1], reverse=True))

def makeCodebook():

    decbook = { '5':'a','2':'b','#':'d','8':'e','1':'t','3':'g','4':'h','6':'i','0':'l','9':'m','*':'n','%':'o','=':'p','(':'r', ')':'s', ';':'t', '?':'u', '@':'v',':':'y','7':' ','-':'y',"'":'s'}
    encbook = { }
    for k in decbook:

        val = decbook[k]
        encbook[val] = k
        
    return encbook, decbook

def decrypt( msg, decbook ):
    for c in msg:
        if c in decbook:
            msg = msg.replace( c, decbook[c] )
    return msg

if __name__ == '__main__':

    msg = '53%%#305))6*;4826)4%=\')4%);806*;48#8@60\'))85;1%(;:-%*8#83(88)5*#;46(;88*96*?;8)*%(;485);5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4\')-485#528806*81(%9;48;(88;4(%?34;48)4%;161;:188;%?;'
    encbook, decbook = makeCodebook()

    frequency_analysis(msg)
    
    deciphertext = decrypt(msg, decbook)
    print(deciphertext)
