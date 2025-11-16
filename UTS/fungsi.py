import os

def create_directory(directory):            #membuat direc
    if not os.path.exists(directory):
        os.mkdir(directory)

def write_to_file(path, data):              #menulis data ke file   
    with open(path,'a') as file:
        file.write(data + '\n')

def read_data(path, limit):                 #membaca data dari file  
    with open(path,'rt') as file:
        count = 0
        for line in file:
            if count == limit:
                break
            if line == "\n":
                continue
            else:
                count += 1
                print(line.replace("\n",""))
                

def does_file_exist(path):                  #memeriksa apakah file ada
    return os.path.isfile(path)

def remove_file(path):                      #removefile
    if does_file_exist(path):               #memeriksa apakah file ada
        os.remove(path)
        print("file berhasil dihapus")      #jika file ada
    else:
        print("file tidak ada")             #jika file tidak ada
        return False