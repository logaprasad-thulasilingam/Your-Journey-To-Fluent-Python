def reverser():
    try:
        lines = []
        with open ("test.txt", "r") as f:
            lines = f.readlines()
            # print (lines)
            f.close()
        with open ("test.txt","w") as f:
            for line in lines[::-1]:
                f.writelines(line.rstrip("\n") + "\n")
                # f.write()
            print("File reversed")
    except FileNotFoundError:
        print("Error: File Not Found")

reverser()