with open("poems.txt", "r") as my_file:
    file_data = my_file.read()
    words = len(file_data)
    wordlist = file_data.split()
    Characters = len(wordlist)
    print("Characters in file :",Characters)
    print("Words in file :",words)
    if("Twinkle" in file_data):
        print("Twinkle is Present !")
    else:
        print("Twinkle is not Present !")
        
