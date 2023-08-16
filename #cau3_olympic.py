#cau3_tao mảng ngẫu nhiên không trùng lăp. Và đếm số phần tử là số nguyên tố

import random
import math

def ktra_snt(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

def create_array(length,min,max):
    array=[]
    while len(array)<length:
        number=random.randint(min,max)
        if number not in array:
            array.append(number)
    return array

while True:
    try:
        
        while True:
            try:
                length=int(input("Nhap so luong phan tu cho array:"))
                if length>=1:
                     break
                else:
                     print("Vui long nhap lại gia tri duong")
            except ValueError:
                print("Nhap so nguyen cho do dai")
    


        min=int(input("Nhap gioi han Trai:"))
        max=int(input("Nhap gioi han Phai:"))
        if length>abs(max)-abs(min)+1:
            print("Khong the tao array khong trung lap.")
            print("Vui long nhap lai")
            continue
        array=create_array(length,min,max)
        print("Mang ngua nhien khong trung lap:",array)
        
        
        count=0
        for number in array:
            if ktra_snt(number):
                count+=1
        print("So luong SNT trong mang la:",count)
        break
    except ValueError:
        print("Da xay ra loi cu phap vui long nhap lai")

while True:
    try:
        choice = input("Bạn có muốn nhập thêm lần nữa? (yes/no): ")
        if choice.lower() == "yes":
                while True:
                    try:
        
                        while True:
                            try:
                                length=int(input("Nhap so luong phan tu cho array:"))
                                if length>=1:
                                    break
                                else:
                                    print("Vui long nhap lại gia tri duong")
                            except ValueError:
                                print("Nhap so nguyen cho do dai")
    


                        min=int(input("Nhap gioi han Trai:"))
                        max=int(input("Nhap gioi han Phai:"))
                        if length>abs(max)-abs(min)+1:
                            print("Khong the tao array khong trung lap.")
                            print("Vui long nhap lai")
                            continue
                        array=create_array(length,min,max)
                        print("Mang ngua nhien khong trung lap:",array)
        
                        count=0
                        for number in array:
                            if ktra_snt(number):
                                count+=1
                                print("So luong SNT trong mang la:",count)
                                break
                    except ValueError:
                        print("Da xay ra loi cu phap vui long nhap lai")
        
        elif choice.lower() == "no":
            print("Kết thúc chương trình.")
            break
        else:
            print("Vui lòng nhập 'yes' hoặc 'no'.")
    except ValueError:
        print("Không phải là lựa chọn hợp lệ. Vui lòng nhập lại.")