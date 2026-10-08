list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Ta đi tạo 1 function để mã hóa chuỗi
def encryption():
    tu_can_ma_hoa = list(str(input("Nhập chuỗi cần mã hóa: ")).lower())
    shift = int(input("Nhập số lượng ký tự muốn dịch chuyển: "))
    tu_da_ma_hoa = "" 
    for char in tu_can_ma_hoa:
        if char in list1:
            vi_tri = list1.index(char)
            vi_tri_moi = (vi_tri + shift) 
            tu_da_ma_hoa += list1[vi_tri_moi]
        else: 
            tu_da_ma_hoa += " "
    print("Chuỗi sau khi mã hóa là: ", tu_da_ma_hoa)
#Ta đi tạo 1 function để giải mã chuỗi
def decryption():
    tu_can_giai_ma = list(str(input("Nhập chuỗi cần giải mã: ")).lower())
    shift = int(input("Nhập số lượng ký tự muốn dịch chuyển: "))
    tu_da_giai_ma = "" 
    for char in tu_can_giai_ma:
        if char in list1:
            vi_tri = list1.index(char)
            vi_tri_moi = (vi_tri - shift) 
            tu_da_giai_ma += list1[vi_tri_moi]
        else: 
            tu_da_giai_ma += " "
    print("Chuỗi sau khi giải mã là: ", tu_da_giai_ma)

#Ta đi chạy chương trình
a =  str(input("Bạn muốn mã hóa hay giải mã chuỗi? (Nhập 'mahoa' hoặc 'giaima'): ")).lower()
if a == "mahoa":
    encryption()
elif a == "giaima":
    decryption()


  
           
 