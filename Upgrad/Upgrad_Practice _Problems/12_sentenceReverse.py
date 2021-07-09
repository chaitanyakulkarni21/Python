# Q.12 WAP to accept a sentence from the user and reverse its each word

quote = input("Type a quote: ")
quoteList = quote.split()
print("Quote: ",quote)
print("Reverse: ",quote[::-1])
print(' ')
print("Quote List: ",quoteList)
for i in quoteList:
    print(i[::-1], end = " ")