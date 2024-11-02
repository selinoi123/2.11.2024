#START
count_a = 0
count_b = 0
count_c = 0
count_d = 0

while True:
    answer: str = str(input("Enter your answer (a, b, c, d): "))
    if answer == 'x':
        break
    elif answer == 'a':
        count_a += 1
    elif answer == 'b':
        count_b += 1
    elif answer == 'c':
        count_c += 1
    elif answer == 'd':
        count_d += 1
    else:
        print("Invalid input, please enter a, b, c, d or 'x'.")

print(f"Number of 'a' answers: {count_a}")
print(f"Number of 'b' answers: {count_b}")
print(f"Number of 'c' answers: {count_c}")
print(f"Number of 'd' answers: {count_d}")
#END
