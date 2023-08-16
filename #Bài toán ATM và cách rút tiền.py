#Bài toán ATM và cách rút tiền

def withdraw_money():
    while True:
        try:
            money=int(input(">>Nhap so tien can rut: (rut toi da 5tr va toi thieu 50k)"))
            if money>5000000 and money<50000:
                print(">>So tien ban rut khong dung yeu cau.Vui long nhap lai!")
                continue
            break
        except ValueError:
            print("Sai cu phap!")
            print("Vui long nhap so nguyen duong")

    denominations=[500000, 200000,100000, 50000, 20000, 10000, 5000, 2000, 1000]
    number_money=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(denominations)):
        number_money[i]=money//denominations[i]
        money%=denominations[i]

    print("So tien rut:")
    for i in range(len(denominations)):
        if number_money[i]>0:
            print(f"So to menh gia {denominations[i]: ,.0f} VND: {number_money[i]} to")

    while True:
        try:
            more = input("Bạn có muốn rut thêm lần nữa? (yes/no): ")
            if more.lower() == "yes":
                while True:
                    try:
                        money=int(input(">>Nhap so tien can rut: (rut toi da 5tr va toi thieu 50k)"))
                        if money>5000000 and money<50000:
                            print(">>So tien ban rut khong dung yeu cau.Vui long nhap lai!")
                            continue
                        break
                    except ValueError:
                        print("Sai cu phap!")
                        print("Vui long nhap so nguyen duong")

                denominations=[500000, 200000,100000, 50000, 20000, 10000, 5000, 2000, 1000]
                number_money=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    
                for i in range(len(denominations)):
                    number_money[i]=money//denominations[i]
                    money%=denominations[i]

                print("So tien rut:")
                for i in range(len(denominations)):
                    if number_money[i]>0:
                        print(f"So to menh gia {denominations[i]: ,.0f} VND: {number_money[i]} to")
            elif more.lower() == "no":
                print("Kết thúc chương trình.")
                break
            else:
                print("Vui lòng nhập 'yes' hoặc 'no'.")
        except ValueError:
            print("Không phải là lựa chọn hợp lệ. Vui lòng nhập lại.")


while True:
    try:
        print("Welcome to ATM!!")
        print(">>>>>MENU<<<<<<")
        print("  1.Rut tien")
        print("  2.Thoat")

        choice=int(input("Nhap lua chon cua ban:"))
        if choice==1:
            withdraw_money()
        elif choice==2:
            print("Xin cam on quy khach!")
            break
        else:
            print("Vui long nhap lai!")
    except ValueError:
        print("Sai cu phap vui long chon dung chuc nang")