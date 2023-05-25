
print("Enter your average marks")
averageMarks = float(input())


if averageMarks >= 90:
    print("A+")
elif averageMarks >= 80:
    print("A")
elif averageMarks >= 65: 
    print("B")
elif averageMarks >= 45:
    print("C")
elif averageMarks >= 35:
    print("D")
else:
    print("F")

if averageMarks >= 35:
    print("Congratulations")
else:
    print("Better luck next time")
