
# 2.1 Part 1

Hal = list(range(51))
print(Hal)

# 2.2 Part 2
def square_numbers(Hal):
    return [i**2 for i in Hal]
square_Hal = square_numbers(Hal)

# 2.3 Part

def get_odd_numbers(list_A, list_B):
    combined_list = list_A + list_B
    odd_integers = [num for num in combined_list if num % 2 != 0]
    odd_integers.sort()
    return odd_integers

list_A = list(range(1,11))
list_B = list(range(20,31))

print(get_odd_numbers(list_A, list_B))

#3 2D List 
#3.1part 1

matrix = []

for i in range(5):
    row = []  
    for j in range(5):
        row.append((i+1)*(j+1)) 
    matrix.append(row) 
for row in matrix:
    print(row)

#3.2 part 2
    
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] = '?'

for row in matrix:
    print(row)

#4 More list practice 
    
def removeDuplicates(lst):
    return list(set(lst))

lst = [1,1,2,3,4,4]
print(removeDuplicates(lst))


