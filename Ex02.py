USER_ACCOUNT_BALANCE = 10000000
ATM_VAULT_BALANCE = 50000000
WITHDRAWAL_FEE = 1100
MULTIPLE_UNIT = 50000

def display_balances():
    """Hiển thị số dư hiện tại của tài khoản và ATM."""
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {USER_ACCOUNT_BALANCE:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {ATM_VAULT_BALANCE:,} VND")

def deposit_money(amount):
    """
    Thực hiện nạp tiền vào tài khoản.
    :param amount: Số tiền cần nạp (int)
    """
    global USER_ACCOUNT_BALANCE, ATM_VAULT_BALANCE
    
    if amount <= 0:
        print("Lỗi: Số tiền nạp phải lớn hơn 0.")
        return
        
    USER_ACCOUNT_BALANCE += amount
    ATM_VAULT_BALANCE += amount
    print(f"Nạp tiền thành công! Số dư mới: {USER_ACCOUNT_BALANCE:,} VND.")

def validate_withdrawal(amount):
    """
    Kiểm tra các quy tắc rút tiền.
    :param amount: Số tiền khách hàng muốn rút.
    :return: Trạng thái (string) và thông báo lỗi (nếu có).
    """
    if amount <= 0:
        return False, "Số tiền phải lớn hơn 0."
    if amount % MULTIPLE_UNIT != 0:
        return False, f"Số tiền rút phải là bội số của {MULTIPLE_UNIT:,} VND."
    if (amount + WITHDRAWAL_FEE) > USER_ACCOUNT_BALANCE:
        return False, "Số dư tài khoản không đủ (bao gồm phí giao dịch)."
    if amount > ATM_VAULT_BALANCE:
        return False, "Máy ATM không đủ tiền mặt."
    
    return True, "Hợp lệ"

def execute_withdrawal(amount):
    """
    Thực thi trừ tiền từ tài khoản và kho chứa ATM.
    :param amount: Số tiền thực rút.
    """
    global USER_ACCOUNT_BALANCE, ATM_VAULT_BALANCE
    
    total_deduction = amount + WITHDRAWAL_FEE
    USER_ACCOUNT_BALANCE -= total_deduction
    ATM_VAULT_BALANCE -= amount
    
    print("\n>>> Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {WITHDRAWAL_FEE:,} VND")
    print(f"Bạn đã rút: {amount:,} VND.")
    print(f"Số dư còn lại: {USER_ACCOUNT_BALANCE:,} VND.")

def main():
    """Hàm điều khiển luồng chính của ứng dụng ATM."""
    while True:
        print("\n" + " SMART ATM ".center(50, "="))
        print("1. Xem số dư\n2. Nạp tiền\n3. Rút tiền\n4. Kết thúc")
        print("=" * 50)
        
        choice = input("Lựa chọn của bạn: ")
        
        if choice == '1':
            display_balances()
            
        elif choice == '2':
            try:
                amt = int(input("Nhập số tiền cần nạp: "))
                deposit_money(amt)
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
                
        elif choice == '3':
            try:
                amt = int(input("Nhập số tiền cần rút: "))
                is_valid, message = validate_withdrawal(amt)
                if is_valid:
                    execute_withdrawal(amt)
                else:
                    print(f"Giao dịch thất bại: {message}")
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
                
        elif choice == '4':
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
