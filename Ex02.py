user_account_balance = 10000000
atm_vault_balance = 50000000

def display_balances():

    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def deposit_money(amount):

    if amount <= 0:
        print("Số tiền không hợp lệ.")
        return False
    
    global user_account_balance, atm_vault_balance
    
    user_account_balance += amount
    atm_vault_balance += amount
    
    print("Giao dịch thành công!")
    print(f"Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
    return True

def check_withdrawal_rules(amount):

    if amount <= 0:
        return "INVALID_AMOUNT"
    
    if amount % 50000 != 0:
        return "MULTIPLE_ERROR"
    
    fee = 1100
    total_deduction = amount + fee
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    
    return "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):

    global user_account_balance, atm_vault_balance
    
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

def main():

    while True:
        print(" SMART ATM ".center(50, "="))
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("="*50)
        
        try:
            choice = input("Vui lòng chọn giao dịch (1-4): ")
            
            if choice == '1':
                display_balances()
            
            elif choice == '2':
                try:
                    amount_str = input("--- NẠP TIỀN ---\nNhập số tiền muốn nạp: ")
                    amount = int(amount_str)
                    deposit_money(amount)
                except ValueError:
                    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
            
            elif choice == '3':
                try:
                    amount_str = input("--- RÚT TIỀN ---\nNhập số tiền cần rút: ")
                    amount = int(amount_str)
                    
                    status = check_withdrawal_rules(amount)
                    
                    if status == "INVALID_AMOUNT" or status == "MULTIPLE_ERROR":
                        if status == "INVALID_AMOUNT":
                            print("Số tiền không hợp lệ.")
                        else:
                            print("Số tiền rút phải là bội số của 50,000.")
                    
                    elif status == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                    
                    elif status == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    
                    elif status == "OK":
                        fee = 1100
                        total_deduction = amount + fee
                        execute_withdrawal(total_deduction, amount)
                
                except ValueError:
                    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
            
            elif choice == '4':
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break
            
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
                
        except KeyboardInterrupt:
            print("\nĐã thoát chương trình.")
            break

if __name__ == "__main__":
    main()