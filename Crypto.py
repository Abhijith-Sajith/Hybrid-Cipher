import random

class encrypt:
    def __init__(self):
        pass

    def gen_key(self):
        k1 = random.randint(1,9)
        k2 = random.randint(1,9)
        k3 = random.randint(1,9)
        return k1, k2, k3
    
    def sub_cipher(self, arr):
        x, y, z = self.gen_key()
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if i == j:
                    arr[i][j] += y
                elif i < j:
                    arr[i][j] += x
                else:
                    arr[i][j] += z
        return arr
    
    def pos_arr_gen(self, arr):
        gen_arr = []
        #arr_ = self.sub_cipher(arr)
        for i in range(arr.shape[0]):
            gen_arr.append(random.randint(1,9))
        return gen_arr
    
    def pos_cipher(self, arr):
        e_arr = self.pos_arr_gen(arr)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                arr[i][j], arr[i][(j+ e_arr[j]) % arr.shape[0]] = arr[i][(j+ e_arr[j]) % arr.shape[0]], arr[i][j]
        return arr

    def re_read(self,arr):
        list_ = []
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                list_.append(arr[i][j])
        return list_
    
    def enc_txt(self, arr):
        txt = ""
        list_ = self.re_read(arr)
        for i in list_:
            txt += chr(i)

        return txt
    

class decrypt:
    def __init__(self):
        pass
    