import random
dice=[]
count=[0,0,0,0,0,0]
for i in range (100):
    dice.append(random.randint(1,6))
    match dice[i]:
        case 1:
            count[0] +=1
        case 2:
            count[1] +=1
        case 3:
            count[2] +=1
        case 4:
            count[3] +=1
        case 5:
            count[4] +=1
        case 6:
            count[5] +=1
print("Número 1 foi conseguido",count[0],"vezes.")
print("Número 2 foi conseguido",count[1],"vezes.")
print("Número 3 foi conseguido",count[2],"vezes.")
print("Número 4 foi conseguido",count[3],"vezes.")
print("Número 5 foi conseguido",count[4],"vezes.")
print("Número 6 foi conseguido",count[5],"vezes.")
