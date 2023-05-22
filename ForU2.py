
def word_processing():
    s = input('Enther the line: ')
    l = len(s)

    #Skip the 3rd character
    for index , c in enumerate(s):
        if index == 2:
            continue
        
    #Index from 0 to 2, not including the character with index 2   
    if c == "c":
        print("There is a 'c' character in the string")
    jk = s[:2] + s[3:]

    print('String lenght: ', l)
    print("A string without the third character: ", jk)
    print("A string without the last character: ", s[:-1])

if __name__ == "__main__":
    word_processing()





