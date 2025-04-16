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

def validDupli(users,phone):
   for person in users:
      if person['phonenumber']== phone:
        return False
    return phone

#hàm nhập thông tin danh bạ
def get_user_input(users):
    
        
    while True:
      name = input('Vui lòng nhập tên: ')
      if validName(users,name):
         break
      else:print("Tên bạn nhập bị trùng lặp")
    

    while True:
       phonenumber = input('Vui lòng nhập số điện thoại: ')
       if validPhone(phonenumber):
        break
       else:print("Bạn nhập sai định dạng sđt vui lòng nhập lại vd:0353634530")
    
    
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

#hàm xem toàn bộ thông tin liên hệ
def read_alluser (users):
    if not users:
        print("Không có liên hệ nào.")
        return

    print("\n Danh sách liên hệ:")
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. Tên: {user['name']}")
        print(f"   SĐT: {user['phonenumber']}")
        print(f"   Email: {user['email']}\n")

# # hàm cập nhật thông tin liên hệ
# def update_user(users):
    
    
   
#các hàm xóa thông tin liên hệ
def findPersonByName(nametarget,users):
   for person in users:
      if person["name"]== nametarget:
        return person
   
   return print("Tên bạn nhập không có trong danh bạ")

def delete_user(filename,users):
    if not users:
        print("Không có liên hệ nào để xoá.")
        return
    else:
       name_to_delete = input('Nhập tên muốn xóa trong danh bạ: ')
       dicttarget= findPersonByName(name_to_delete,users)
    #    print(f"{dicttarget}")
       users.remove(dicttarget)
    #    newPhoneBook =[ item for item in users if item.get("name") != name_to_delete]
       
    #    print(f"{data}")

    save_user_to_file(filename,users)
    #    print(f"{newPhoneBook}")

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
       update_user(users)
     elif choice == '4':
       delete_user(filename,users)
     elif choice == '5':
        break

main()
