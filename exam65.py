import random

hanguls = ("가나다라마바사아자차카타파하")
hanguls = str(hanguls)

with open('info.txt','w') as file:
    for i in range(1000):
        name=random.choice(hanguls)+random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        print(name+"\n")
        file.write(f"{name},{weight},{height}\n")


# with open('text.txt','r') as file:
#     print(file.read())

