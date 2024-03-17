print("Hi welcome to my program\nIts is a personality checker program")
print("Do you want to check your personality?")
print("Just type yes or no...")
a=input("yes or no?")
if a=="yes":
    print("Congratulations now you can take personality test\n ok so choose one of the given numbers")
    numbers=[1,2,3,4,5,6,7,8,9]
    for numbers in numbers:
        print(numbers)
    x=int(input("which number you want to choose?"))
    if x==1:
        print("you are:\n loveable\n appealing\n selfish\n ambitious")
    elif x==2:
        print("you are:\nperfectionism\nintuitive\nemotional\nsensitive")
    elif x==3:
        print("you are:\nfunny\noutgoing\negotistical\nsuperior")
    elif x==4:
        print("you are:\ndependable\nreliable\nstubborn\nexcels")
    elif x==5:
        print("you are:\nenerfatic\nenthusiastic\ndrama\nexcitable")
    elif x==6:
        print("you are:\ndevious\nfunny\nkind\ncaring")
    elif x==7:
        print("you are:\ncalm\nwise\nimpatient\ncritical")
    elif x==8:
        print("you are\nstable\nenthusiastic\nmature\nestablished")
    elif x==9:
        print("you are:\nfriendly\nmoody\ncharasmatic\nattractive")
    else:
        print("choose the number between 1 and 9")    
elif a=="no":
    print("no worries you can go :)")
else:
    print("please choose one of them \n yes \n no")
print("Thankx for using my program\n Have a good day:)")







