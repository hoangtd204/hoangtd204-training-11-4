

#function
def CaculatingEvenNumberbySum(numbers): 
 even_sum = sum([x for x in numbers if x % 2 == 0])
 return even_sum


def CaculatingEvenNumberbyFor(numbers): 
    even_for = 0
    for x in numbers:
        if x % 2 == 0:
            even_for += x
    return even_for

#Variable
list_number = [1, 2, 3, 4, 5, 6, 7, 8]

# call function
tongbySum = CaculatingEvenNumberbySum(list_number)
tongbyFor = CaculatingEvenNumberbyFor(list_number)

#Result
print("Tổng số chẵn tính bằng sum:", tongbySum)
print("Tổng số chẵn tính bằng for:", tongbyFor)
