

def openFile(path):

    file = open(path)
    lines = file.readlines()
    return lines


def main():

    path = "README.md"
    list = openFile(path)
    print(list)

if __name__ == "__main__":
    main()