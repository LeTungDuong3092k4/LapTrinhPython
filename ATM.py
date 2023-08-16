class ATM:
    def __init__(self):
        self.balance = 100000000  # Số dư ban đầu
        self.total_withdrawals = 0
        self.total_amount_withdrawn = 0

    def withdraw(self, amount):
        if self.total_withdrawals >= 10:
            print("Vượt qua số lần rút tối đa (10 lần). Không thể rút thêm.")
            return False

        if self.total_amount_withdrawn + amount > 50000000:
            print("Vượt qua số tiền rút tối đa (50,000,000 VND). Không thể rút thêm.")
            return False

        if amount > self.balance or amount < 50000 or amount > 5000000:
            print("Số tiền rút không hợp lệ. Vui lòng nhập lại.")
            return False

        denominations = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]
        number_money = [0] * len(denominations)

        for i, denom in enumerate(denominations):
            number_money[i] = amount // denom
            amount %= denom

        self.balance -= sum([number * denom for number, denom in zip(number_money, denominations)])
        self.total_withdrawals += 1
        self.total_amount_withdrawn += sum([number * denom for number, denom in zip(number_money, denominations)])
        return number_money

    def get_balance(self):
        return self.balance


def main():
    atm = ATM()
    denominations = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]

    while True:
        try:
            print("Chào mừng bạn đến với máy ATM!!")
            print(">>>>>MENU<<<<<<")
            print("  1. Rút tiền")
            print("  2. Xem số dư")
            print("  3. Thoát")

            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice == 1:
                if atm.total_withdrawals >= 10:
                    print("Vượt qua số lần rút tối đa (10 lần). Không thể rút thêm.")
                    continue

                if atm.total_amount_withdrawn >= 50000000:
                    print("Vượt qua số tiền rút tối đa (50,000,000 VND). Không thể rút thêm.")
                    continue

                amount_to_withdraw = int(input("Nhập số tiền cần rút: "))
                result = atm.withdraw(amount_to_withdraw)
                if result:
                    print("Số tiền rút:")
                    for i, number in enumerate(result):
                        if number > 0:
                            print(f"Số tờ mệnh giá {denominations[i]:,.0f} VND: {number} tờ")
                else:
                    print("Không thể rút tiền.")
            elif choice == 2:
                balance = atm.get_balance()
                print(f"Số dư hiện tại: {balance:,.0f} VND")
            elif choice == 3:
                print("Kết thúc chương trình.")
                break
            else:
                print("Vui lòng nhập lựa chọn hợp lệ.")
        except ValueError:
            print("Sai cú pháp. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()
