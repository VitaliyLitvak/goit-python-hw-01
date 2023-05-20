import os, shutil, re


path = input('Ввведіть будь-ласка шлях до папки:')
path = os.path.normpath(path)

def normalize(file_name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    file_name = re.sub(r"\W", "_", file_name)
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    file_name = ''.join(TRANS.get(ord(ch), ch) for ch in file_name)
    return file_name

def proccessing(path):
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            file_name, file_ext = os.path.splitext(item) 
            file_ext = file_ext.lower()
            normalize(file_name)
            images = ('.jpeg', '.png', '.jpg', '.svg')
            documents = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
            audio = ('.mp3', '.ogg', '.wav', '.amr')
            video = ('.avi', '.mp4', '.mov', '.mkv')
            archives = ('.zip', '.gz', '.tar')
            if file_ext in images:
                os.makedirs(os.path.join(path, 'images'), exist_ok=True)
                os.rename(os.path.join(path, item), os.path.join(path, 'images', item)) 
            elif file_ext in documents:
                os.makedirs(os.path.join(path, 'documents'), exist_ok=True)
                os.rename(os.path.join(path, item), os.path.join(path, 'documents', item)) 
            elif file_ext in audio:
                os.makedirs(os.path.join(path, 'audio'), exist_ok=True)
                os.rename(os.path.join(path, item), os.path.join(path, 'audio', item))     
            elif file_ext in video:
                os.makedirs(os.path.join(path, 'video'), exist_ok=True)
                os.rename(os.path.join(path, item), os.path.join(path, 'video', item))  
            elif file_ext in archives:
                try:
                    os.makedirs(os.path.join(path, 'archives'), exist_ok=True)
                    os.rename(os.path.join(path, item), os.path.join(path, 'archives', item))
                    shutil.unpack_archive(os.path.join(path, 'archives', item), os.path.join(path, 'archives', file_name))
                except shutil.ReadError:
                    continue      
            else:
                continue
            
  
def sorter(path):
    ignore_list = ('archives', 'video', 'audio', 'documents', 'images')
    items = os.listdir(path)
    print(items)
    for item in items:
        item_path = os.path.join(path, item)
        item_path = os.path.normpath(item_path)
        if os.path.isdir(item_path) and item not in ignore_list:
            sorter(item_path)
            if not os.listdir(item_path):
                os.rmdir(item_path)
        elif os.path.isfile(item_path):
            print('f -' + item_path)
            proccessing(path)      

sorter(path)


