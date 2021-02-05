items = ["Dan", "Mark", "Bob"]


def demo():
    try:

        # file = open("people.txt", "w+")
        with open("people.txt" , "w+") as file:
        
            for item in file.readlines():
                items.append(item.rstrip())

            contents = print(file.read())
            return contents

    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))

    except Exception as e:
        print('An error occurred: ' + str(e))

    # finally:
    #     file.close()

def view_demo():

    with open("people.txt", "w") as file:

        for item in items:
            file.write(str(item) + "\n")
        # contents = print(file.read())
        # return contents
    
        file = open("people.txt", "r")
        contents = file.read()
        print(contents)


# demo()
view_demo()
