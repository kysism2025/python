numbers = [5,15,6,20,7,25]

for number in numbers:
    if number >= 10 :
        print(f"{number} ",end="")
    else:
        continue

for number in numbers:
    if number < 10:
        continue
    else:
        print(f"{number} ",end="")

        