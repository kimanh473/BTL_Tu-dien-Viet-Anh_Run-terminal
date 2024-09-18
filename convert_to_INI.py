import configparser

dictionary = {} # Khởi tạo một dictionary (kiểu dữ liệu) để lưu dữ liệu từ điển

# Xử lí kí tự "%" trong file .txt
with open('TuDien_VietAnh23460.txt', 'r+', encoding='utf-8') as f: 
    content=f.read()
    content=content.replace("%","%%")
    f.seek(0) # Đưa con trỏ về đầu file
    f.write(content)
    f.close()
with open('TuDien_VietAnh23460.txt', 'r', encoding='utf-8') as file:
    
    # Khởi tạo các biến mặc định
    current_word = None
    current_definition = ""
    
    for line in file:
        line = line.strip()
        
        # Kiểm tra nếu đầu dòng bắt đầu bằng @ thì thực hiện tách từ 
        if line.startswith('@'):
            if current_word:
                dictionary[current_word] = {'Definitions': current_definition.strip()}
            
            current_word = line[1:]

            current_definition = "" 
        else:
            current_definition += line + '\n' 
    
    if current_word:
        dictionary[current_word] = {'Definitions': current_definition.strip()}
    file.close()
    
# Khởi tạo đối tượng ConfigParser
config = configparser.ConfigParser()

# Lưu các section, key, value vào config
for word, data in dictionary.items():
    config.add_section(word)
    config.set(word, 'Definitions', data['Definitions'])

# Lưu dữ liệu vào tệp
with open('TuDien_VietAnh.ini','w',encoding='utf-8') as ini_file:
    config.write(ini_file)
    ini_file.close()
print("Đã convert file sang file .ini")



