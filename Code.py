import numpy as np
from Functions import Fnctn
from Crypto import encrypt


text = input("Enter your text to be encrypted: ")
list1 = []
for i in text:
    list1.append(ord(i))

obj = Fnctn(len(list1))
x = obj.nrst_sqrt(len(list1))
filled = obj.arr_fill(len(list1), list1)
arr = np.array(filled)
new = arr.reshape(x,x)
crypt = encrypt()
x = crypt.sub_cipher(new)
sub = crypt.pos_cipher(x)
y = crypt.enc_txt(sub)
print("Encrypted Text: ", y)