#!python3

#author: @musa_sana
#contact: musana.net

def xor():
    print("*"*150)
    inp = input("Your Data: ")
    key = input("Your Key : ")
    key2 = ""
    out = ""
    inp2bin = ""
    key2bin = ""
    out2bin = ""

    if (not inp.isnumeric()) or (not key.isnumeric()):
    	exit("Only number value accepted. Your data type is invalid. Quiting...")

    for i in range(len(str(inp))):
    	split_inp = int(str(inp)[i])
    	split_key = int(key[i % (len(key))])

    	tempout = str(split_inp ^ split_key) 
    	out += str(split_inp ^ split_key)   
    	key2 += key[i % (len(key))]

    	out2bin += str(bin(int(tempout)))[2:]+" "
    	inp2bin += str(bin(split_inp))[2:]+" "
    	key2bin += str(bin(split_key))[2:]+" "


    a = inp2bin.split(" ")
    b = key2bin.split(" ")
    c = out2bin.split(" ")
        
    x = list()
    y = list()
    z = list()

    for i in range(len(a)):
    	if(len(a[i]) < 4):
    		bul = 4 - len(a[i])
    		x.append(bul*"0"+a[i])
    	else:
    		x.append(a[i])


    	if(len(b[i]) < 4):
    		bul = 4 - len(b[i])
    		y.append(bul*"0"+b[i])
    	else:
    		y.append(b[i])


    	if(len(c[i]) < 4):
    		bul = 4 - len(c[i])
    		z.append(bul*"0"+c[i])
    	else:
    		z.append(c[i])

    x.pop()
    y.pop()
    z.pop()

    print('''\n Data: \t {data} \t\t binData: {binstr} \n Key: \t {key} \t\t bin.Key: {binkey}\n {line}\n XOR: \t {xor} \t\t bin.Xor: {binxor}\n'''.
    	format(data=inp, binstr=' '.join(x), key=key2, binkey=' '.join(y), xor=out, binxor=' '.join(z), line="-"*150), end="*"*150)

    print("\n"*3)



while(True):
	xor()
