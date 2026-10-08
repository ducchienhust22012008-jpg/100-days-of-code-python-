import random
print("chào mừng đến với trò chơi đoán số!")
print("Tôi đã chọn một số từ 1 đến 100. Hãy dự đoán xem đó là số nào?")
secret_number = random.randint(1, 100)
difficulty = input("Chọn mức độ khó (easy or hard): ").lower()
if difficulty == "easy":
    attempts = 10
    print("Bạn có 10 lượt đoán.")
elif difficulty == "hard":
    attempts = 5
    print("Bạn có 5 lượt đoán.")
else:
    print("Mức độ không hợp lệ. Vui lòng chọn 'easy' hoặc 'hard'.")
    exit()
def check_guess():
    global attempts
    while attempts > 0:
        guess = int(input("Nhập dự đoán của bạn: "))
        if guess == secret_number:
            print(f"Chúc mừng! Bạn đã đoán đúng số {secret_number}.")
            exit()
        elif guess < secret_number:
            print("Số bạn đoán quá thấp.")
            attempts -= 1
            print(f"Bạn còn {attempts} lượt đoán.")
        else:
            print("Số bạn đoán quá cao.")
            attempts -= 1
            print(f"Bạn còn {attempts} lượt đoán.")
    print(f"Rất tiếc! Bạn đã hết lượt đoán. Số đúng là {secret_number}.")
check_guess()