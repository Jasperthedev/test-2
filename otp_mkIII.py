def code():
    uncoded = input('please input unencoded phrase: ')
    coder = input('please put code word: ')

    #first lists
    uncodedlist = list(uncoded)# unencrypted word list
    wordlistcd = list(coder) #list of coding numbers

    # corresponding number generators
    # message
    x = 0
    messagenumlist = [] # coresponding numbers of the message
    while x < len(uncodedlist):
        messagenumlist.append(ord(uncodedlist[x])-96)# makes words into numbers
        x += 1
    #coding word to numbers 
    xcd = 0
    wordlistcd2 = [] #coresponding numbers
    while xcd < len(wordlistcd):
        wordlistcd2.append(ord(wordlistcd[xcd])-96)# makes words into numbers
        xcd += 1
        
    CodingNumberListLengthened = [] #code number list lengthed
    while len(CodingNumberListLengthened)< len(messagenumlist):
        CodingNumberListLengthened.extend(wordlistcd2)#lengthens list of codeword numbers

    
    while len(CodingNumberListLengthened)> len(messagenumlist):#shortens if too long
        CodingNumberListLengthened.pop(-1)

    finalwordlist = [sum(i) for i in zip(messagenumlist, CodingNumberListLengthened)] #adds the two list
    counter2 = 0
    while counter2 < len(finalwordlist):# no numbers over 26
        if finalwordlist[counter2] > 26:
            finalwordlist[counter2] = finalwordlist[counter2] - 26
        counter2 += 1
    countteerr = 0
    
    for i in finalwordlist: #converts back to letters
        placeholder = finalwordlist[countteerr] + 96
        finalwordlist[countteerr] = chr(placeholder)
        countteerr += 1
    print("this is your coded word:")
    print("".join(finalwordlist))


def uncode():
    #print(choice)

    CodedMessage = list(input ("please input the coded word: "))
    codeword = input ("please input code word: ")
    #print (codedlist)
    #print(type(codedlist))
    #codedlist2 = list(map(str.strip, codedlist.strip('][').replace('"', '').split(',')))# supposed to turn a stringlist into a list somehow
    #print(type(codedlist2))

    #processes code word into suitable list:
    ListedCodeWord = list(codeword) #listing the codeword
    counter = 0
    ListedCodeWordNumbers = [] #codeword numbers
    while counter < len(ListedCodeWord):
        ListedCodeWordNumbers.append(ord(ListedCodeWord[counter])-96)# makes codewordlist into numbers
        counter += 1

    # turns text coded word into list of numbers
    counter = 0
    CodedMessageNumbers = [] #coded message numbers
    while counter < len(CodedMessage):
        CodedMessageNumbers.append(ord(CodedMessage[counter])-96)# makes codewordlist into numbers
        counter += 1
    #makes the list a suitable length
    ListedCodeWordNumbersLengthend = []
    while len(ListedCodeWordNumbersLengthend) < len(CodedMessageNumbers):
        ListedCodeWordNumbersLengthend.extend(ListedCodeWordNumbers)#lengthens list of codeword numbers
        
    while len(ListedCodeWordNumbersLengthend)> len(CodedMessageNumbers):#shortens if too long
        ListedCodeWordNumbersLengthend.pop(-1)
    counter2 = 0
    semifinallist = [] #number list that has yet to be converted
    finallist = [] #final number list
    count = 0
    for i in ListedCodeWordNumbersLengthend:
        #if type(i) == str:

        #print(i)
        ListedCodeWordNumbersLengthend[count] = int(ListedCodeWordNumbersLengthend[count])
        #print(type(count))
        
        if count == len(ListedCodeWordNumbersLengthend):
            break
        count += 1
    #print(CodedMessageNumbers)
    #print(ListedCodeWordNumbersLengthend)
    while counter2 < len(CodedMessageNumbers):# no negative numbers
        semifinallist.append(CodedMessageNumbers[counter2] - ListedCodeWordNumbersLengthend[counter2] )
        if semifinallist[counter2] < 1:
            semifinallist[counter2] = semifinallist[counter2] + 26
        counter2 += 1

    countteerr = 0
    
    for i in semifinallist: #converts back to letters
        placeholder = semifinallist[countteerr] + 96
        semifinallist[countteerr] = chr(placeholder)
        countteerr += 1
        
    print("this is the uncoded word: ")
    print("".join(semifinallist))#semifinallist
    #print(cnvtedcdlist)
    #print(cdl)



while True:
    choice = input('please pick 1 encode or 2 decode : ')
    if choice == '1':
        code()
    elif choice == '2':
        uncode()
    else:
        print("please select 1 or 2")
    Breakquestion = input("do you want to exit? if you do type yes: ")
    if(Breakquestion == "yes"):
        break
