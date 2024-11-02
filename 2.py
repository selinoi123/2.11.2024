#START

while True:
    try:
        number:int = int(input("Enter a number between 10 and 99: "))
        if 10 <= number <= 99:
            break
        else:
            print("number is invalid, try again.")
    except ValueError:
        print("Only numbers are allowed. Please try again.")

num2: int = number % 10
num1: int = number // 10

if num2 > num1:
    new_number: int = num2 * 10 + num1
    print(new_number)
else:
    print(number)

#END