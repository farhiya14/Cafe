

my_list =  ["1", "2", "3"]

def menu():
    print("0 for exit\n1 for product menu")






def save_txt():
    f = open('your_file.txt', 'w+')

    for item in my_list:
        f.write(item +"\n")
    f.close()

    
def read_txt():
    with open('your_file.txt', 'r') as f:
        # for item in f.readlines():
            # my_list.append(item.rstrip('\n'))
        contents = print(f.readlines())
        return contents
    
# save_txt()
# read_txt()

def check():
    import os.path

    if os.path.isfile('your_file.txt'):
        return read_txt()

    else:
        save_txt()
        read_txt()

check()


