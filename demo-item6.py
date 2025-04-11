
#Variable
list_number=[56,32,67,34,89,12,8,9]

#function

#Kiểm tra số nguyên tố
def check_PrimeNumber(number):

  if number < 2 :
    
    return f"{number} không phải là số nguyên tố."
  
  else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                
                return f"{number} không phải là số nguyên tố."
           
        return f"{number}  là số nguyên tố."
  
#Tổng các số chẵn trong một danh sách
def CaculatingEvenNumber(numbers): 
 
 even_sum = sum([x for x in numbers if x % 2 == 0])
#  sumreturn =even_sum
#  print("Tổng các số chẵn là:", even_sum)

 return even_sum

#main function
def main():
    while True:
        print("Chọn phần kiểm tra:") 
        print("1. kiểm tra số nguyên tố")
        print("2. tổng các số chẵn trong một danh sách")
        print("3. Bài toán bí mật")
        print("4. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
          try:
            numberinput = int(input("nhập số bạn muốn kiểm tra"))
            print(f"{check_PrimeNumber(numberinput)}")
          except ValueError:
            print("nhập một số nguyên đi cha nội.")
          finally:
              print("hoàn tất kiểm tra số nguyên tố.\n")

        elif choice == '2':
          print(f"{CaculatingEvenNumber(list_number)}")

        elif choice == '3':
          print(f"bài toán là lấy kết quả của bài 2 điểm kiểm tra xem đó có phải số nguyên tố không")
          print(f"{check_PrimeNumber(CaculatingEvenNumber(list_number))}")

        elif choice == '4':
            break
        
        else:
            print(" Lựa chọn không hợp lệ.")

main()