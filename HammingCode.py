import random
import numpy as np
import pandas as pd



def generate_random_ascii():
    for i in range(0,100):
        make_str=list()
        make_ascii=list()
        make_hex=list()
        for j in range(0,4):
            num=random.randint(97,122)
            make_str.append(str(chr(num)))
        string=''.join(make_str)
        binary=bin(int.from_bytes(string.encode(), 'big'))
    return string,binary



def hamming(a,b):
    return len([i for i in filter(lambda x: x[0] != x[1],zip(a,b))])

df=pd.read_csv('sample.csv',names=['word', 'bin'])

for k in range(0, 100):
    string, binary = generate_random_ascii()
    df.iloc[k, 0] = string
    df.iloc[k, 1] = "0" + binary[2:]
df.to_csv('sample.csv', header=False, index=False)





min=10000000
count=0;

for i in range(1,102):
    for j in range(i+1,102):
        count=count+1

        hd=hamming(df.iloc[i,1],df.iloc[j,1])
        print(count,"(",df.iloc[i,0],df.iloc[j,0],") hamming_distance: ",hd)
        if min>hd:
            min=hd

print("min hamming distance",min)




