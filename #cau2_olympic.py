#cau2_tinh tổng các số chia hết cho 2 và 3 nhưng không chia hết cho 5
#xử dụng nguyên lý bù trừ

import time

def tinhtong(n):
    #tổng các số chia hết cho k: sum=(n//k)*(k+(n//k)*k)//2
    sum=0
    sum=(n//2)*(2+(n//2)*2)/2
    sum+=(n//3)*(3+(n//3)*3)/2
    sum-=(n//10)*(10+(n//10)*10)/2
    sum-=(n//15)*(15+(n//15)*15)/2
    sum-=(n//6)*(6+(n//6)*6)/2
    sum+=(n//30)*(30+(n//30)*30)/2
    return sum

def calculate_time(define,n):
    start=time.time()
    define(n)
    end=time.time()
    return end-start
while True:
    try:
        n = int(input("Nhập một số nguyên dương: "))
        if n > 0:
            print("Tổng các số chia hết cho 2 và 3 nhưng không chia hết cho 5 là:",tinhtong(n))
            print(f"Thời gian chạy hết:{calculate_time(tinhtong,n)} giây")
            break
        else:
            print("Số phải là nguyên dương. Vui lòng nhập lại.")
    except ValueError:
        print("Không phải là số nguyên. Vui lòng nhập lại.")


print("Bạn đã nhập một số nguyên dương:", n)
while True:
    try:
        choice = input("Bạn có muốn nhập thêm lần nữa? (yes/no): ")
        if choice.lower() == "yes":
            while True:
                try:
                    n = int(input("Nhập một số nguyên dương: "))
                    if n > 0:
                        break
                    else:
                        print("Số phải là nguyên dương. Vui lòng nhập lại.")
                except ValueError:
                    print("Không phải là số nguyên. Vui lòng nhập lại.")
        elif choice.lower() == "no":
            print("Kết thúc chương trình.")
            break
        else:
            print("Vui lòng nhập 'yes' hoặc 'no'.")
    except ValueError:
        print("Không phải là lựa chọn hợp lệ. Vui lòng nhập lại.")
        
print("Tổng các số chia hết cho 2 và 3 nhưng không chia hết cho 5 là:",tinhtong(n))
print(f"Thời gian chạy hết:{calculate_time(tinhtong,n)} giây")