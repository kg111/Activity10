from random import randrange
import random
import string


number = 16146063
print("0. The student number is: ", number)

def count_primes_in_list(numbers):
    primes = []
    for num in numbers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:                
                is_prime = False
                break

        if is_prime and num!=0 and num!=1:
            primes.append(num)
    return len(primes)


z = [1, 6, 1, 4, 6, 0, 6, 3]
p = int(count_primes_in_list(z))
print ("1. The number of prime numbers in this student number is: ", p)
print("\n")


#create random number 
q = randrange(25,50)
print("2. The random number is: ", q)
print("\n")


#Divide q by p 
r = round(q /p)
print("3. The number of strings to be generated is:", r)
print("\n")


#generate random strings 
print("4. List of strings:")
print("*******************")

def randomString(size=10, chars=string.ascii_lowercase ):
    return ''.join(random.choice(chars) for _ in range(size))


wrdlist =[]
count=0

for x in range (0,r):
    if count % 2 != 0:
        size =7 
    else:
        size = 5 
    count+=1
    wrdlist.append(randomString(size))

for (num, i) in enumerate(wrdlist):
    print(num,"- ", i)
print("*******************")
print("\n")

#Sort List
print("4. Sorted List:")
print("*******************")

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

VowelList=[]

class my_dictionary(dict): 
    def __init__(self): 
        self = dict() 
    def add(self, key, value): 
        self[key] = value 

dict_obj = my_dictionary() 
for word in wrdlist:
    vowels=0
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels+=1
            dict_obj.add(word,vowels)
    print(wrdlist.index(word),"- ", word, "(vowel: ",vowels,")")
print("*******************")
#print(VowelList)
#print(dict_obj)
