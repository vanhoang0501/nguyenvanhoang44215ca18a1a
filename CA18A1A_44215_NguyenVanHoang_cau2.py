"""
Author: Nguyễn Văn Hoàng
Date: 01/11/2021
Problem:cau 2
Solution:
    ....
"""
def Cau2():
    # List chứa các đối tượng
    data = []
    # Số lượng mặt hàng
    n = 0

    class MatHang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():

        # Mở file
        f = open("CA18A1A_44215_NguyenVanHoang_inp.txt", mode="r", encoding="utf-8")

        """  Đọc dữ liệu và đưa vào class """
        n = int(f.readline()) # n la so luong mat hang

        for i in range(n):
            row_data = f.readline().split("|")
            mat_hang = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang) # dua du lieu vao data cac object

        #  Đóng file
        f.close
        print("***"*10)
        print(" > Hoàn thành việc nhập dữ liệu từ file: CA18A1A_44215_NguyenVanHoang2_inp.txt"
              " ")
        print("***" * 10)
    def cv24():
        if len(data) == 0:
            print("Bạn cần chọn nhập thông tin về mặt hàng từ file")
        else:
            # đã có thông tin, xử lý
            print("In thông tin các mặt hàng:")
            print("**" * 20)
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("**"*20)

    def cv25():
        """ Hiển thị mặt hàng có đơn giá cao nhất """
        print("--Mat Hang Dat Nhat--")
        print("**" * 20)
        # Tìm ra mặt hàng có đơn giá cao nhất
        matHangDatNhat = data[0]
        for i in data:
            if i.don_gia > matHangDatNhat.don_gia:
                matHangDatNhat = i
        # Hiển thị ra mặt hàng có đơn giá cao nhất
        matHangDatNhat_str = matHangDatNhat.ma_mat_hang + "|" + matHangDatNhat.ten_mat_hang + "|" + str(matHangDatNhat.so_luong) \
        + "|" + str(matHangDatNhat.don_gia) + "|" + str(matHangDatNhat.thanh_tien)
        print(matHangDatNhat_str)
        print("**"*20)

    def cv26():
        if len(data) == 0:
            print("Bạn cần chọn thông tin về mặt hàng")
        else:
            # Ghi dữ liệu
            f = open("CA18A1A_44215_NguyenVanHoang_out.txt", mode = "w", encoding="utf-8")

            f.write(str(len(data)) + "\n")

            for i in data:
                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                    + "|" + str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                f.write(s)

            f.close()
            print("**" * 20)
            print("Hoàn thành ghi ra file:CA18A1A_44215_NguyenVanHoang_out.txt")
            print("**"*20)




    while True:
        print("---MENU---")
        print("23.Nhập dữ liệu từ file.")
        print("24. In dữ liệu ra màn hình.")
        print("25. In mặt hàng đơn giá cao nhất.")
        print("26. Ghi thông tin vào file.")
        cv = input("Bạn chọn công việc, bấm phím Q để thoát: ")
        if cv == "23":
            cv23()
        elif cv == "24":
            cv24()
        elif cv == "25":
            cv25()
        elif cv == "26":
            cv26()
        elif cv.upper() == "Q":
            break

if __name__ == '__main__':
    Cau2()
