import json
import os
import re

#hàm đọc thông tin đã có trong json file
def read_user_from_file(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            return json.load(f)
    return []

#hàm nhập thông tin danh bạ
def get_user_input():
    name = input('Vui lòng nhập tên: ')
    phonenumber = input('Vui lòng nhập số điện thoại: ')
    email = input('Nhập email:')
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    phone_regex = r'^0\d{9}$'
#regexforphonenumber
    if re.match(phone_regex, phonenumber):
        print(" Số điện thoại hợp lệ!")
        
    else:
        print("Số bạn nhập không đúng định dạng")

#regexforemail        
    if re.match(regex, email):
      print("Email hợp lệ!")
    else:
      print("Email không hợp lệ!")

    user = {
        'name': name,
        'phonenumber': phonenumber,
        'email':email
    }
    return user

#hàm xem toàn bộ thông tin liên hệ
def read_alluser (users):
   

    if not alluser:
        print("Không có liên hệ nào.")
        return

    print("\n Danh sách liên hệ:")
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. Tên: {user['name']}")
        print(f"   SĐT: {user['phonenumber']}")
        print(f"   Email: {user['email']}\n")

#hàm cập nhật thông tin liên hệ
# def update_user(users):
    
    
   
#hàm xóa thông tin liên hệ
# def delete_user(users):
#     if not users:
#         print("Không có liên hệ nào để xoá.")
#         return

#     name_to_delete = input("Nhập tên liên hệ muốn xoá: ").strip().lower()
#     original_len = len(users)
#     new_users = []

#     for user in users:
   
#         name = user['name'].strip().lower()
#         if name != name_to_delete:
#             new_users.append(user)

#     users[:] = new_users  # Cập nhật danh sách gốc

#     if len(users) < original_len:
#         print("Đã xoá liên hệ có tên:", name_to_delete)
#     else:
#         print("Không tìm thấy liên hệ nào với tên đó.")


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
     print("4. Thoát chương trình.")
     
     choice = input("Chọn: ")
     if choice == '1':
       while True:
         user = get_user_input()
         users.append(user)
         save_user_to_file(filename, users)
         conti = input('Bạn có muốn nhập thêm thông tin liên hệ không (y/n)? ')
         if conti.lower() != 'y':
          break
    
     elif choice == '2':
       read_alluser(users)
    
     elif choice == '3':
       delete_user(users)
    
main()
