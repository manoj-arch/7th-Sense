def vowels():
    str = input("Enter the input: ")
    if(str == 'a' or str=='e' or str =='i' or str=='o' or str =='u'
       or str == 'A' or str=='E' or str =='I' or str=='O' or str =='U'):
        print("This is vowel: ",str)
    else:
        print("Not a vowel: ",str)
vowels()