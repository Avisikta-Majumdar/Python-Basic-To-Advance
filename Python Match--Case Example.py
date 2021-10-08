Day = input()
match Day:
    case "Sun":
        print("Today is Sunday")
    case "Mon":
        print("Today is Monday")
    case "Tue":
        print("Today is Tuesday")
    case "Wed":
        print("Today is Wedsnesday")
    case "Thur":
        print("Today is Thursday")
    case "Fri":
        print("Today is Friday")
    case "Sat":
        print("Today is Saturday")
    case _:#This will work when all the case failed this is like default value
        print("Your input is invaild")


'''
Example 1 :-
Sun
Today is Sunday

Example 2:-
Son
Your input is invaild



'''
