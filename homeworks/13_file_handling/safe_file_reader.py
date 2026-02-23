def safe_file_reader():
    try:
        with open("test1.txt", "r") as f:
            print("Test file found successfully...\n")
            lines = f.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("Error: Test file is not available in current directory")
    return None

safe_file_reader()