# WhatsToWear.py
# Billy Ridgeway
#Practicing else if "El-If" statements by calculating grades.

# Creates the variable rainy and asks the user if it's rainy outside. It converts upper case to lower case.
rainy = input("How's the weather? Is it raining (y/n)").lower()

# Creates the variable cold and asks the user if it's cold outside. It converts upper case to lower case.
cold = input("Is it cold outside? (y/n)").lower()

if (rainy == 'y' and cold == 'y'):              # The elif block decides what the user should wear or take with
                                                # them depending on the state of the weather.
    print("You'd better wear a raincoat.")
elif (rainy == 'y' and cold != 'y'):
    print("Carry an umbrella with you.")
elif (rainy != 'y' and cold == 'y'):
    print("Put on a jacket, it's cold out!")
elif (rainy != 'y' and cold != 'y'):
    print("Wear whatever you want, it's beautiful outside!")
