import numpy as np
from Functions import Fnctn
from Crypto import encrypt, decrypt

# Encryption Algorithm
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
z,k1,k2,k3 = crypt.sub_cipher(new)
sub, k4 = crypt.pos_cipher(z)
y = crypt.enc_txt(sub)
print("Encrypted Text: ", y)

# Decryption algorithm
de = decrypt(y)
ord_ = de.read_ciph(y)
array = np.array(ord_)
matrix = array.reshape(x,x)
ret = de.pos_decipher(matrix, k4)
retr = de.sub_decipher(ret,k1,k2,k3)
de_arr = retr.reshape(1,len(ord_))
de_list = [chr(i) for i in de_arr[0] if i != ord("X")]
text = "".join(de_list)

print(text)