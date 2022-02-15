def input_point():
    point = int(input("Enter Grade Point: "))
    # check if the grade point meets the conditions
    if point>10 or point<4:
        print("Invalid grade point! Try Again")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")