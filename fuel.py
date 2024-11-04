#****Code developed by: JOSE ELIGIO FRONTANEZ RIVERA******
# Solution based on the problem Fuel Gauge of the problem set 3 for the course CS50P
# This code will take a fraction in the format x/y and split it so that we can conduct the division operation
# IF after the division, the result is between 0% (Zero percent) and 100% (One-hundred percent), the program will output
# To the user, the percentage left in the tank
# IF the result is 100% (One-Hundred percent) exactly, instead of the value, the program will
# only display the letter "F" to symbolize that the tank is full
# ELSE IF the result is 0% (Zero percent) exactly, instead of the value, the program will
# only display the letter "E" to symbolize that the tank is empty
# ****IF the result would be more than 100% (One-Hundred percent), it will continue to prompt the user for and adequate
# x/y values***
# This program will handle exceptions such that if y is 0 (Zero) or if it's not an integer value or a numerical value,
# It will handle them accordingly and continue to prompt the user for a correct x/y pair values


while True:
    try:
        fraction = (input("Fraction: "))
        numbers = fraction.split(sep="/")
        x = (numbers[0])
        y = (numbers[1])
        result = int((int(x) / int(y)) * 100)
        if result > 0 and result < 100:
            print(f"{result}%")

        if result == 100:
            print("F")
        elif result == 0:
            print("E")

        if result > 100:
            continue
        break
    except (ValueError,ZeroDivisionError) as e:
        print(e)



