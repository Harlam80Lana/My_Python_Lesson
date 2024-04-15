def month_to_season(n):
        
        if (n == 1 or n == 2 or n == 12):
            print("winter")

        elif (n == 3 or n == 4 or n == 5):
            print("spring")

        elif (n == 6 or n == 7 or n == 8):
            print("summer")

        elif (n == 9 or n == 10 or n == 11):
            print("autumn")

        else:
            print("что-то пошло не так ") 

        return n       

n = int(input("введите номер месяца: "))  
    
month_to_season(n)       