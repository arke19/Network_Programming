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
    histo_max = len(byte_array)
    index = 0

    for byte in histo:
        prob_list[index] = byte/histo_max
        index += 1
    
    return prob_list

#https://stackoverflow.com/questions/64803311/how-to-write-a-function-that-returns-probability-distributions-entropy-in-pytho
def entropi(prob):
    entropy = 0
    for i in range(len(prob)):
        if prob[i] > 0:
            entropy += prob[i] * math.log((1/prob[i]), 2) 
    return entropy

histo = makeHisto(byte_array)
probability = makeProb(histo)
#print("histo",histo_in)
probability_sum = sum(probability, 0)
print("probability",probability,"probability sum is",probability_sum)

print(entropi(probability))


t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
t10 = 10*t1


t1Code = zlib.compress(bytearray(t1, "utf-8"))
t10Code = zlib.compress(bytearray(t10, "utf-8"))

print("t1: ", len(t1Code))
print("t10: ", len(t10Code))
print(entropi(makeProb(makeHisto(bytearray(t1, "utf-8")))))
print(entropi(makeProb(makeHisto(bytearray(t10, "utf-8")))))
print(len(t1))
print(len(t10))


print(histo)