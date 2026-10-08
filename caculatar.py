def phep_cong(a, b):
    return a + b
def phep_tru(a, b):
    return a - b
def phep_nhan(a, b):    
    return a * b
def phep_chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b
def tinhtoan():
    if phep_tinh == "+":
        return phep_cong(first_number, second_number)
    elif phep_tinh == "-":
        return phep_tru(first_number, second_number)
    elif phep_tinh == "*":
        return phep_nhan(first_number, second_number)
    elif phep_tinh == "/":
        return phep_chia(first_number, second_number)


trung_gian = True

first_number = float(input("Nhập số thứ nhất: "))
phep_tinh = input("Nhập phép tính (+, -, *, /): ")
second_number = float(input("Nhập số thứ hai: "))

print(tinhtoan())

while trung_gian== True:    
    answer = input("Bạn có muốn tiếp tục không? (y/n): ")
    if answer.lower() == "n":
        trung_gian = False
    elif answer.lower() == "y": 
        first_number = tinhtoan()
        second_number = float(input("Nhập số thứ hai: "))
        phep_tinh = input("Nhập phép tính (+, -, *, /): ")
        print(tinhtoan())
