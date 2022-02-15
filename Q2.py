def Next_date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):
        day=int(input('enter the day:'))
        if(1<=day<=31):
            break
        else:
            print('entered day is invalid')
    while(True):
        month=int(input('enter the month:'))
        if(1<=month<=12):
            break
        else:
            print('entered month is invalid')
    while(True):
        year=int(input('enter the year:'))
        if(1800<=year<=2025):
            break
        else:
            print('enter year from 1800 to 2025 only')
    if month in list1:
        if(day==31):
            day=1
            month+=1
            print(day,'/',month,'/',year)
        elif(day<31):
            day+=1
            print(day,'/',month,'/',year)
        else:
            print('invalid date,try again')
            Next_date()
    elif month in list2:
        if(day==30):
            day=1
            month+=1
            print(day,'/',month,'/',year)
        else:
            print('invalid date,try again')
            Next_date()
    elif month in list3:
        if(year % 4 == 0):
            if(day==29):
                day=1
                month=month+1
                print(day,'/',month,'/',year)
            elif(day<29):
                day+=1
                print(day,'/',month,'/',year)
            else:
                print('invalid date ,try again')
                Next_date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,'/',month,'/',year)
            elif(day<28):
                day+=1
                print(day,'/',month,'/',year)
            else:
                print('invalid date,try again')
                Next_date()
    elif month in list4:
        if(day==3):
            day=1
            month=1
            year+=1
            print(day,'/',month,'/',year)
        elif(day<31):
            day+=1
            print(day,'/',month,'/',year)
            Next_date()
        else:
            print('invalid date,try again')
            Next_date()
    else:
        print('invalid date,try again')
        Next_date()
Next_date()
print('\n')
    
            


            