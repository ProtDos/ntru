import NTRU2
import time

"""
This is a benchmark test to see how fast and efficient the different modes of security of the algorith is. 
The result is the average out of the test (10 is default) and is rounded to two number after comma.
"""

#######################
number_of_test = 10
#######################


def middle(num_list):
    if len(num_list) == 0:
        return None
    summe = 0
    for zahl in num_list:
        summe += zahl
    return summe / len(num_list)


l1 = []
l2 = []
l3 = []

for i in range(number_of_test):
    print(f"1. Round {i+1}/{number_of_test}")
    a = time.time()
    NTRU2.generate_keys("test", mode="moderate")
    l1.append(time.time()-a)

    b = time.time()
    enc = NTRU2.encrypt("test", "hello world")
    l2.append(time.time()-b)

    c = time.time()
    dec = NTRU2.decrypt("test", enc)
    l3.append(time.time()-c)

l11 = []
l21 = []
l31 = []

for i in range(number_of_test):
    print(f"2. Round {i + 1}/{number_of_test}")
    a = time.time()
    NTRU2.generate_keys("test", mode="high")
    l11.append(time.time() - a)

    b = time.time()
    enc = NTRU2.encrypt("test", "hello world")
    l21.append(time.time() - b)

    c = time.time()
    dec = NTRU2.decrypt("test", enc)
    l31.append(time.time() - c)

l112 = []
l212 = []
l312 = []

for i in range(number_of_test):
    print(f"3. Round {i + 1}/{number_of_test}")
    a = time.time()
    NTRU2.generate_keys("test", mode="highest")
    l112.append(time.time() - a)

    b = time.time()
    enc = NTRU2.encrypt("test", "hello world")
    l212.append(time.time() - b)

    c = time.time()
    dec = NTRU2.decrypt("test", enc)
    l312.append(time.time() - c)

a1 = middle(l1)
a2 = middle(l2)
a3 = middle(l3)
print("Moderate Security:")
print(f"Key generation: {round(a1, 2)}s")
print(f"Encryption: {round(a2, 2)}s")
print(f"Decryption: {round(a3, 2)}s\n")
# print(a1, a2, a3)

b1 = middle(l11)
b2 = middle(l21)
b3 = middle(l31)
print("High Security:")
print(f"Key generation: {round(b1, 2)}s")
print(f"Encryption: {round(b2, 2)}s")
print(f"Decryption: {round(b3, 2)}s\n")
# print(b1, b2, b3)

c1 = middle(l112)
c2 = middle(l212)
c3 = middle(l312)
print("Highest Security:")
print(f"Key generation: {round(c1, 2)}s")
print(f"Encryption: {round(c2, 2)}s")
print(f"Decryption: {round(c3, 2)}s\n")
# print(c1, c2, c3)

"""   BENCHTEST
MODERATE:
- Key Generation: ~0.9sec
- Encryption: ~0.05sec
- Decryption: ~0.08sec

HIGH:
- Key Generation: ~2sec
- Encryption: ~0.1sec
- Decryption: ~0.18sec

HIGHEST:
- Key Generation: ~25.5sec
- Encryption: ~1.5sec
- Decryption: ~2.5sec
"""
