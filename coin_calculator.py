def pennies(user_pennies):
    number_of_pennies = (user_pennies * (.01))
    return (number_of_pennies)

def nickels(user_nickels):
    number_of_nickels = ((user_nickels) * (.05))
    return(number_of_nickels)

def dimes(user_dimes):
    number_of_dimes = ((user_dimes) * (.1))
    return(number_of_dimes)

def quarters(user_quarters):
    number_of_quarters = ((user_quarters) * (.25))
    return(number_of_quarters)

def total (pennies , nickels , dimes , quarters):
    total = ((pennies) + (nickels) + (dimes) + (quarters))
    return (total)


user_pennies = int(input("Input number of pennies: "))
pennies = pennies(user_pennies)

user_nickels = int(input("Input number of nickels: "))
nickels = nickels(user_nickels)

user_dimes = int(input("Input number of dimes: "))
dimes = dimes(user_dimes)

user_quarters = int(input("Input number of quarters: "))
quarters = quarters(user_quarters)

total = total(pennies , nickels , dimes , quarters)
print (total)
