import math
import random
import zlib

text = open("Labb9/exempeltext.txt", "r")
txt = text.read()
byte_array = bytearray(txt, "utf-8")
byte_array_copy = byte_array.copy()
random.shuffle(byte_array_copy)

code_compress = zlib.compress(byte_array)
code_compress_copy = zlib.compress(byte_array_copy)




print(len(str(txt)))
print(len(byte_array))
print(len(byte_array_copy))
print(len(code_compress))
print(len(code_compress_copy))


def makeHisto(byte_array):
    histo_list = [0]*256
    for byte in byte_array:
        histo_list[byte] += 1

    return histo_list

def makeProb(histo):
    prob_list = [0]*256
    byte_array_size = len(byte_array)
    index = 0

    for byte in histo:
        prob_list[index] = byte/byte_array_size
        index += 1
    
    return prob_list

#https://stackoverflow.com/questions/64803311/how-to-write-a-function-that-returns-probability-distributions-entropy-in-pytho


def entropi(prob):
    entropy = 0
    for i in range(len(prob)):
        if prob[i] > 0:
            entropy += prob[i] * math.log((1/prob[i]), 2) 
    return entropy

probability = makeProb(makeHisto(byte_array))
probability_sum = sum(probability, 0)
print("probability",probability,"probability sum is",probability_sum)

print(entropi(probability))


t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
t10 = 10*t1


t1Code = zlib.compress(bytearray(t1, "utf-8"))
t10Code = zlib.compress(bytearray(t10, "utf-8"))

print("t1:", len(t1Code))
print("t10:", len(t10Code))
print(entropi(makeProb(makeHisto(bytearray(t1, "utf-8")))))
print(entropi(makeProb(makeHisto(bytearray(t10, "utf-8")))))
print(len(t1))
print(len(t10))



print(entropi(makeProb(makeHisto(code_compress))))
print(entropi(makeProb(makeHisto(code_compress_copy))))
print(entropi(makeProb(makeHisto(byte_array))))
print(entropi(makeProb(makeHisto(byte_array_copy))))


"""
9.2
1c 
Adding single characters to a string adds only a byte to the size of the string itself, but every string takes up 40 bytes on its own.

The bytearray contains more bytes than the string because UTF-8 () uses 1-4 bytes to represent a character

Can also be due to swedish letters not being in utf-8

2d
We can not expect it to be less than the entropy 4.6, because that is the average swedish bits/symbol.

4c
The shuffled bytearray is 30500 bytes and compressed its 19800 bytes, 158400 bits and 5.6 bits/symbol

4d
The unshuffled bytearray is 30500 bytes and compressed its 12800 bytes, 102400 bits and 3.9 bits/symbol

4e
The randomized compressed copy has the biggest bits/symbol, 
and the compressed copy which was not randomized has the smallest bits/symbol. 
This is because when it is compressed, 
some pattern can be used to predict certain things in the array that was not shuffled.

9.3
b t1 is 68 bytes when compressed, and t10 is 78.
c The difference between t1 and t10 is small because in t10 the pattern is the same, 
just longer. This means that predicting what follows will be easy compress tool.
"""
