#Number 1
import re
import numpy as np

def reverse_alphabet(letters) :
    numbers = re.findall(r'\d+',letters)
    alphabet = re.findall(r'[a-zA-Z]+',letters)
    result = ''.join(alphabet)[::-1] + ''.join(numbers)
    return result
print("NUMBER 1")
print(reverse_alphabet("NEGIE1"))
print("////////////////////////\n")


#Number 2
def longest_word(sentences): 
    longest = max(sentences.split(), key=len)
    return longest, len(longest)

print("NUMBER 2")
result = longest_word("Saya sangat senang mengerjakan soal algoritma")
print(result[0] , ":" , result[1] , "karakter")
print("////////////////////////\n")

print("NUMBER 3")

def something(QUERY, INPUT):
    result = []
    for i in QUERY:
        for j in INPUT:
            if i == j:
                result.append(i)
    return result
    
INPUT = ['xc', 'dz', 'bbb', 'dz']  
QUERY = ['bbb', 'ac', 'dz']  

myList = something(QUERY, INPUT)
result = {}
for i in myList:
    result[i] = myList.count(i)
print(result)
print("////////////////////////\n")


print("NUMBER 4")

def matrix_operation(matrix):
    first_diagonal = np.diagonal(matrix)
    second_diagonal = np.fliplr(matrix).diagonal()
    difference = sum(first_diagonal) - sum(second_diagonal)
    print("diagonal pertama: ", first_diagonal[0], "+", first_diagonal[1],"+", first_diagonal[2],"=", sum(first_diagonal))
    print("diagonal kedua: ", second_diagonal[0], "+", second_diagonal[1],"+", second_diagonal[2],"=", sum(second_diagonal))
    print("maka hasilnya adalah ", sum(first_diagonal),"-", sum(second_diagonal), "=", difference)

matrix_operation(np.array([[1, 2, 0], [4, 5, 6], [7, 8, 9]]))
print("////////////////////////\n")





            