print("List Comprehensions:")
# 1. print the sq of all the numbers in a list of numbers 1 to 11 using list comprehensions
sq = [x**2 for x in range(1,11)]
print("Square List:",sq)
print(' ')

# 2. Convert the weights in kg
weight_in_pounds = [110,210,215,180,119]
weight_in_kg = [w*0.45 for w in weight_in_pounds]
print("Weight in Kg: ", weight_in_kg)
print(' ')

#3. Extract the words containing *
giftBox = 'pencil mac*book rubber i*phone paper i*pad'
giftList = [gift for gift in giftBox.split() if '*' in gift]
print("Gift List: ",giftList)
print(' ')

print("Dictionary Comprehensions: ")
#4. Print the following dictionary using comprehensions
# {1: 'ola', 2: 'ola', 3: 'ola'}
d = {x:'ola' for x in range(1,4)}
print(d, end = " ")

#5. Print the following dictionary using comprehensions {x: x**2} 
sqDictionary = {x:x**2 for x in range(1,10)}
print("Square Dictionary: ",sqDictionary)
print(' ')

#6. capitalize all the strings in the given list
colors = ['red','yellow','blue','cyan','indigo','magenta']
print("Capitalize:",[color.capitalize() for color in colors])
print("Upper case:",[color.upper() for color in colors])
print("Reverse:",[color[::-1] for color in colors])
