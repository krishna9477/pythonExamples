def main():
    uppercase_count = 0
    lowercase_count = 0
    digits_count = 0
    whitespace_count = 0

    uppercase =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    whitespace = [' ']
    infile = open(r'C:\Users\Ismail\Downloads\file.txt',"r")
    data = infile.readlines()
    d1=str(data)

    for character in d1:
        if character  in uppercase:
            uppercase_count += 1

    for character in d1:
        if character in lowercase:
            lowercase_count += 1

    for character in d1:
        if character in digits:
            digits_count += 1

    for character in d1:
        if character in whitespace:
            whitespace_count += 1

    print('The uppercase count is',uppercase_count)
    print('The lowercase count is',lowercase_count)
    print('The digit count is',digits_count)
    print('The whitespace count is',whitespace_count)

main()