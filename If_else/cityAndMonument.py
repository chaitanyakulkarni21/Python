# Accept any city from the user and print the monument present in that city
'''
City            Monument

Delhi            Red Fort
Agra             Taj Mahal
Jaipur           Jal Mahal
'''

city = input("Enter city: ")
if city == "Delhi":
    print("Red Fort")
elif city == "Agra":
    print("Taj Mahal")
elif city == 'Jaipur':
    print("Jal Mahal")
else:
    print("Enter any city from Delhi, Agra and Jaipur..")
