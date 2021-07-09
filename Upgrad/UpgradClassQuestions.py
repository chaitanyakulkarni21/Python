# Q.1 Split the string and convert it into a list
msg = 'Pizza is better than donut'
msgList = msg.split()
print("List: ",msgList)
# Q.2 Convert the list into string
sep = '-'
print('String:',sep.join(msgList))
print(' ')

# Q.3 Change the word amazing to awesome in the list
quote = 'python is an amazing programming language'
print("Quote: ",quote)
quoteList = quote.split()
print("Quote List: ",quoteList)
quoteList[3] = 'awesome'
print('Updated list:',quoteList)
sep = " "
print('String:',sep.join(quoteList))
print(' ')

# Q.4 Extract the #strings
tweet = '#Laziness is the #mother of all the bad habits but ultimately she is the mother and we should #respect it'
tweetList = tweet.split()
for string in tweetList:
  if string.startswith('#'):
    print(string, end = " ")
print(' ')

# Q.5 Prepare a new list named vowel words and store only the words that starts with vowel
funnyJoke = 'Me and my bed are perfect for each other but alarm clock keeps trying to break us up'
jokeList = funnyJoke.split()
vowelWords = []
print("Joke list: ",jokeList)
for string in jokeList:
  if string[0] in 'aeiouAEIOU':
    vowelWords.append(string)
print('Vowel words list:',vowelWords)
print(' ')
print("The above can be implemented using list comprehension: ")
vowelWords = [string for string in jokeList if string[0] in 'aeiouAEIOU']
print('Vowel Words list: ',vowelWords)
print(' ')

# Q.6 Extract the otp from the given text
otpText = 'Your swiss bank money transfer one time password is 425844 , Swiss Bank'
otpList = otpText.split()
print("OTP List: ",otpList)
for string in otpList:
  if string[0].isdigit():
    print("OTP:",string)
print(' ')

# Q.7 Given this nested list, use indexing to grab the word "hello" **
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print("List:",lst)
print(lst[3][1][2][0])
print(' ')

# Q.8 Grab the word hello in the following dictionary
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print('Dictionary: ',d)
print(d['k1'][3]['tricky'][3]['target'][3])

# Q.9 Return the sum and avg of the digits that appear in the given string
str1 = 'English = 78 Science = 83 Maths = 68 History = 65'
numbers = []
strList = str1.split()
print("String list: ",strList)
# for string in strList:
#   if string[0].isdigit():
#     numbers.append(int(string))
# print("Numbers: ",numbers)
numbers = [int(string) for string in strList if string[0].isdigit()]
print("Numbers: ",numbers)
print("Sum: ",sum(numbers))
print("Average: ",sum(numbers)/len(numbers))
print(' ')