import random
#khởi tạo bộ bài
bo_bai = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def tinh_toan1():
    i = input("Bạn có muốn rút thêm bài không? (y/n): ")
    if i == "y":
        player_cards.append(random.choice(bo_bai))
        print(f"Bạn có các lá bài: {player_cards}, tổng điểm là: {sum(player_cards)}")
        if sum(player_cards) > 21:
            print("Bạn đã thua!")
            exit()
        else:
            tinh_toan1()
    if i == "n":
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(bo_bai))
        print(f"Nhà cái có các lá bài: {dealer_cards}, tổng điểm là: {sum(dealer_cards)}")        
        if sum(dealer_cards) > sum(player_cards):
            print("Bạn đã thua!")
            exit()
        elif sum(dealer_cards) < sum(player_cards):
            print("Bạn đã thắng!")
            exit()
        else:
            print("Hòa!")
            exit()

i = input("Bạn đã sẵn sáng chơi chưa? (y/n): ")
if i == "y":
    #random ra 2 lá bài cho người chơi và 2 lá bài cho nhà cái
    player_cards = []
    dealer_cards = []
    for so_nguyen in range(2):
        player_cards.append(random.choice(bo_bai))
        dealer_cards.append(random.choice(bo_bai))
    print(f"Bạn có các lá bài: {player_cards}, tổng điểm là: {sum(player_cards)}")
    print(f"Lá bài đầu tiên của nhà cái là: {dealer_cards[0]}")
    trung_gian = True
    while trung_gian == True:
        tinh_toan1()
        