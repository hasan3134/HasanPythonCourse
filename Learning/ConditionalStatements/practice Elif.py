import datetime
print("Enter your std")
std=int(input())
print("enter your avrage Marks")
avrageMarks = float(input())

if avrageMarks >=90:
    print("A+")
elif avrageMarks >=80:
    print("A")
elif avrageMarks >=65:
    print("B")
elif avrageMarks >= 50:
    print("C")
elif avrageMarks >=35:
    print("D")
else:
    print("F")
    
if avrageMarks >=35:
    print("congratulation you are pass your welcome in new class:)")
    print("your next std will be",std+1)
    print("For Stationary Pay Fee ")
    if std <= 1:
        print("2000")
    elif std<= 2:
        print("2500")
    elif std <= 3:
        print("3000")
    elif std <=4:
        print("3500")
    elif std <=5:
        print("4000")
    elif std <=6:
        print("4500")
    elif std <=7:
        print("5000")
    elif std <=8:
        print("6000")
    elif std <=9:
        print("8000")
    elif std <=10:
        print("commrerce=9500|science=1100")
    elif std <=11:
        print("commerce=10500|science=12000")

else:
    print("you are fail better luck next time and try to give retest:(")
    print("For Retest Fill A question")
    print("Enter Your Mobile Number")
    MobileNumber=float(input()) 
    date = datetime.date.today()     
    print("Retest Date was",date)
    print("come at 11A.M In school on Given Date")




    