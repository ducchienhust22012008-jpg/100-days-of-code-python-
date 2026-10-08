import os
data = {}
chan_ly = True
print('''
                         ___________
                        
           )_______(
           |"""""""|_.-._,.---------.,_.-._
           |       | | |               | | ''-.
           |       |_| |_             _| |_..-'
           |_______| '-' `'---------'` '-'
           )"""""""(
          /_________\\
        .-------------.
       /_______________\\
''')
while chan_ly==True:
    gia_tri_chung_gian = input("Nhập tên người tham gia đấu giá: ")
    data[gia_tri_chung_gian] = int(input("Nhập số tiền muốn đấu giá: $"))
    gia_tri_chan_ly = input("còn ai tham gia đấu giá không? (Nhập có hoặc không): ")
    if gia_tri_chan_ly == "không":
        chan_ly = False
    elif gia_tri_chan_ly == "có":
        os.system('cls')
maximum = 0
for key in data:
    if data[key] > maximum:
        maximum = data[key]
        winner = key
print("Người thắng cuộc là: ", winner, "với số tiền đấu giá là: $", maximum) 


