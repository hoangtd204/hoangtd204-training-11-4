import json
import os
import re

#hàm đọc thông tin đã có trong json file
def read_user_from_file(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            return json.load(f)
    return []


#requireforEmail
def validEmail(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
# #requireName
def validName(users,name):
    for person in users:
        if person['name']== name:
         return False
    return name  
   
#requireforPhoneNumber
def validPhone(phone):
    pattern = r'^0\d{9}$'  
    
    return re.match(pattern, phone)

def validDupli(users, phone):
    for person in users:
        if person['phonenumber'] == phone:
            return False
    return True

#hàm nhập thông tin danh bạ
def get_user_input(users):
    
        
    while True:
      name = input('Vui lòng nhập tên: ')
      if validName(users,name):
         break
      else:print("Tên bạn nhập bị trùng lặp")
    

    while True:
       phonenumber = input('Vui lòng nhập số điện thoại: ')
       if validPhone(phonenumber) and validDupli(users, phonenumber):
        break
       
       else:
        print("Bạn nhập sai định dạng hoặc đã bị trùng lặp")
    
    
    while True:
       email = input('Vui lòng nhập email: ')
       if validEmail(email):
        break
       else:print("Bạn nhập sai định dạng email vui lòng nhập lại vd:tangduchoang34@gmail.com")

    user = {
        'name': name,
        'phonenumber': phonenumber,
        'email':email
    }
    return user

#Hàm xem toàn bộ thông tin liên hệ
def read_alluser (users):
    if not users:
        print("Không có liên hệ nào.")
        return

    print("\n Danh sách liên hệ:")
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. Tên: {user['name']}")
        print(f"   SĐT: {user['phonenumber']}")
        print(f"   Email: {user['email']}\n")

#Các hàm cập nhật thông tin liên hệ

def get_input_to_update(filename,dicttarget_to_update,users):

    while True:
        newName= input('Nhập tên mới:  ')
        if validName(users,newName):
            dicttarget_to_update['name']=newName
            save_user_to_file(filename,users)  
            break
        else:
            print("Tên mới không hợp lệ") 
    while True:
        newEmail= input('Nhập email mới:  ')
        if validEmail(newEmail):
           dicttarget_to_update['email']=newEmail
           save_user_to_file(filename,users)  
           break
        else:
          print("Email mới không hợp lệ")
    while True:
        newPhoneNumber= input('Nhập sđt mới:  ')
        if validPhone(newPhoneNumber) and validDupli(users,newPhoneNumber):
            dicttarget_to_update['phonenumber']=newPhoneNumber
            save_user_to_file(filename,users)  
            break
        else:
            print("Số điện thoại mới không hợp lệ")





def update_user(filename,users):
    if not users:
        print("Không có liên hệ nào để cập nhật.")
        return
    else:
       name_to_update = input("Nhập tên của thông tin liên hệ  bạn muốn update thông tin:  ")
       dicttarget_to_update = findPersonByName(name_to_update,users)
       if dicttarget_to_update:
         get_input_to_update(filename,dicttarget_to_update,users)
       else :
            print("Tên bạn nhập không có trong danh bạ")

            
#Các hàm xóa thông tin liên hệ
def findPersonByName(nametarget,users):
   for person in users:
      if person["name"]== nametarget:
        return person
   
   return None

def delete_user(filename,users):
    if not users:
        print("Không có liên hệ nào để xoá.")
        return
    else:
       name_to_delete = input('Nhập tên muốn xóa trong danh bạ: ')
       dicttarget_to_delete= findPersonByName(name_to_delete,users)
       if  dicttarget_to_delete:
         users.remove(dicttarget_to_delete)
         save_user_to_file(filename,users)  
         print("Tên bạn nhập đã bị xóa trong danh bạ")
       else :
          print("Tên bạn nhập không có trong danh bạ")
          



#hàm lưu thông tin vào file json

def save_user_to_file(filename, users):
    with open(filename, 'w') as f:
        json.dump(users, f, indent=4)


def main():
    filename = 'users.json'
    users = read_user_from_file(filename)

    while True:
     print("Chọn hành động thực hiện") 
     print("1. Thêm liên hệ.")
     print("2. Xem liên hệ.")
     print("3. Cập nhật thông tin liên hệ.")
     print("4. Xóa liên hệ.")
     print("5. Thoát chương trình.")
     
     choice = input("Chọn: ")
     if choice == '1':
      while True:
         user = get_user_input(users)
         users.append(user)
         save_user_to_file(filename, users)
         conti = input('Bạn có muốn nhập thêm thông tin liên hệ không (y/n)? ')
         if conti.lower() != 'y':
          break
    
     elif choice == '2':
       read_alluser(users)
    
     elif choice == '3':
       update_user(filename,users)
     elif choice == '4':
       delete_user(filename,users)
     elif choice == '5':
        break

main()
