print("Welcome to KBC, Lets,start playing!")

print("Do you want to play?")
play= input("Enter yes or no :")
if play == "no":
    print("Okay thanks for joining!")
elif play =="yes":
    questions= [
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1],
    ["Who is the supreme court of home","Mother","Father","Son","Daughter",1]
            ]
    levels= [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]

    money=0

    for i in range(0,len(questions)):
        question= questions[i]
        print(f"\n\nQuestion no. {i+1} for Rs. {levels[i]}:")
        print(f"a. {question[1]}              b. {question[2]}")
        print(f"c. {question[3]}                 d. {question[4]}")
        reply =int(input("Enter your answer (1-4) 0 to quit"))  
        if (reply== 0):
            money = levels[i-1]
            break

        if (reply == question[-1]):
            print(f"\nCorrect answer, you have won Rs. {levels[i]}")
            if (i== 4):
                money=10000
            elif (i==9):
                money=320000
            elif (i==14):
                money=7500000
            elif (i==16):
                money=75000000
        
        else:
            print("\nWrong answer!")
            break

                      
    print(f"\n\nCongratulations! , Your take home money is {money}")

else:
    raise ValueError ("Invalid Value!")


