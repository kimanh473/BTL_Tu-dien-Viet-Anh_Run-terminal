import datetime
import configparser

# Ghi lại nhật kí thao tác
def write_log(Mode,Content):
    f=open("log.txt",mode=Mode,encoding='utf-8')
    f.write(f"{Content}")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    f.write(f"~ Thời gian: {timestamp}\n")
    f.close()
    
# Lựa chọn 2: thêm từ và lưu vào nhật kí
def add_word():
    thong_tin_end=""
    thong_tin_list=[]
    tu_tv=input("\nNhập vào từ tiếng Việt cần thêm:\n- Nhấn Enter để thoát nhập từ, quay về bảng Menu\nXin mời nhập: ")
    tu_tv=tu_tv.strip().lower()
    if tu_tv=="":
        return False
    config1 = configparser.ConfigParser()
    config1.read('TuDien_VietAnh.ini',encoding='utf-8')

    # Kiểm tra từ nhập vào đã có trong từ điển chưa
    if tu_tv in config1.sections():
        print(f"\n'{tu_tv}' đã tồn tại trong từ điển. Không thể thêm từ!\n")
        thong_tin_end="Từ đã tồn tại trong từ điển. Không thể thêm từ!"
        lich_su2=f"""
@   Thêm từ Tiếng Việt: {tu_tv}
    Kết quả: {thong_tin_end}\n"""
        write_log('a',lich_su2)
        return False

    # Nhập vào các loại từ, nghĩa và ví dụ
    list_lt=[]
    while True:
        list_lt_temp=[]
        thong_tin_lt=""
        lt=input("\n~Nhập vào loại từ:\n- Nhấn Enter để thoát nhập loại từ, lưu từ vào từ điển và quay về nhập từ mới\n- Nhấn Space nếu từ không có loại từ, sau đó ấn Enter để chuyển sang nhập nghĩa\nXin mời nhập: ")
        if lt=="":
            break
        thong_tin_lt+="* "+lt+"\n"

        while True:
            thong_tin_eng=""
            eng=input("\n~Nhập vào nghĩa:\n- Nhấn Enter để thoát nhập nghĩa, quay về nhập loại từ mới\n- Nhấn Space nếu từ không có nghĩa, ấn Enter để chuyển sang nhập ví dụ\nXin mời nhập: ")
            if eng=="":
                break
            thong_tin_eng+="- "+eng
            thong_tin_vd=""
            list_vd=[]

            while True:
                vd=input("\n~Nhập vào ví dụ\n- Ví dụ có dạng: ví dụ tiếng Việt+ví dụ sau khi dịch sang tiếng Anh\n- Nhấn Enter để thoát nhập ví dụ, quay về nhập nghĩa mới\nXin mời nhập: ")
                if vd=="":
                    break
                list_vd.append(vd)
                
            thong_tin_vd="="+"\n=".join(list_vd)+"\n"
            thong_tin_eng+="\n"+thong_tin_vd
            thong_tin_lt+=thong_tin_eng
            
        list_lt_temp.append(thong_tin_lt)
        list_lt.append(list_lt_temp)

    # Phá danh sách con trong list_lt
    for sublist in list_lt:
        thong_tin_list+=sublist
    thong_tin_end="".join(thong_tin_list)

    # Chỉnh sửa đối với các từ không có loại từ, nghĩa hoặc ví dụ
    thong_tin_end=thong_tin_end.replace("*  \n","").replace("-  \n","").replace("=\n","")
    
    # Tạo đối tượng ConfigParser
    config2=configparser.ConfigParser()
    
    # Thêm một từ điển mới
    config2[tu_tv]={'Definitions':thong_tin_end}

    # Ghi lại các thay đổi vào file
    with open('Tudien_VietAnh.ini', 'a',encoding='utf-8') as configfile:
        config2.write(configfile)
        configfile.close()
        
    # Lưu nhật kí
    lich_su2=f"""
@   Thêm từ Tiếng Việt: {tu_tv}
    Kết quả:
{thong_tin_end}"""
    write_log('a',lich_su2)

    return True

# Lựa chọn 1: tra từ và lưu vào nhật kí
def search_word():
    tu_tv_tra=input("\nNhập từ tiếng Việt cần tra (nhấn Enter để thoát tra từ): ")
    tu_tv_tra=tu_tv_tra.strip().lower()
    if tu_tv_tra=='':
        return False
    
    #Tạo đối tượng ConfigParser
    config1 = configparser.ConfigParser()
    config1.read('TuDien_VietAnh.ini',encoding='utf-8')
    
    #Kiểm tra, đưa ra kết quả cho từ nhập vào
    if tu_tv_tra in config1.sections():
        print(f"\n~Infomation of '{tu_tv_tra}' is found in the dictionary~")
        for key, value in config1.items(tu_tv_tra):
            value=value.replace("* "," ~Loại từ: ").replace("=","Ví dụ: ").replace("+","\n\tEx: ")
            print(f"Thông tin từ:\n\n{value}")
            
    # Lưu nhật kí
        lich_su=f"""
@   Tra từ Tiếng Việt: {tu_tv_tra}
    Kết quả:
    Thông tin từ:
{value}\n"""
        write_log('a',lich_su)

    else:
        ket_qua="Không tìm thấy từ trong từ điển"
        print(f"{ket_qua}")
        print("Đã tra xong từ và ghi vào lịch sử")
 
    # Lưu nhật kí
        lich_su1=f"""
@   Tra từ Tiếng Việt: {tu_tv_tra}
    Kết quả: {ket_qua}\n"""
        write_log('a',lich_su1)

    return True

# Main: Bảng Menu
while True:
    print("MENU:")
    print("1. Tra từ")
    print("2. Bổ sung từ mới")
    print("3. Kết thúc chương trình")
    
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        while search_word():
            pass
        print("Đã kết thúc tra từ, quay lại menu \n")   
    elif choice == "2":
        while add_word():
            pass
        print("Đã kết thúc nhập từ mới, quay lại menu \n")
          
    elif choice == "3":
        print("Kết thúc chương trình!")
        break
    else:
        print("Nhập sai, vui lòng nhập lại!\n")

