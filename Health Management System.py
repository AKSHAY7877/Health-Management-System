#Health Management System By Akshay Sharma
print("\t\t\tHealth Management System\n")
print("Press 1 for retrieve(get details) and 2 for write")
inp = int(input())

print("Choose the person")
print("Press 1 for Harry\nPress 2 for Akshay\nPress 3 for Hammad")
name = int(input())

print("Choose from food and exercise Press 1 for food and 2 for exercise")
val = int(input())

def retrive(name, val):
    if name == 1:
        if val == 1:
            f = open("harry_food.txt")
            print("Food Details of Harry are")
            print(f.read())
            print("Details read successfully")
            f.close()
        elif val == 2:
            f = open("harry_exercise.txt", "r")
            print("Exercise Details of Harry are")
            print(f.read())
            print("Details read successfully")
            f.close()
        else:
            print("Invalid Input")
    elif name == 2:
        if val == 1:
            f = open("akshay_food.txt", "r")
            print("Food Details of Akshay are")
            print(f.read())
            print("Details read successfully")
            f.close()
        elif val == 2:
            f = open("akshay_exercise.txt", "r")
            print("Exercise Details of Akshay are")
            print(f.read())
            print("Details read successfully")
            f.close()
    elif name == 3:
        if val == 1:
            f = open("hammad_food.txt", "r")
            print("Food Details of Hammad are")
            print(f.read())
            print("Details read successfully")
            f.close()
        elif val == 2:
            f = open("hammad_exercise.txt", "r")
            print("Exercise Details of Hammad are")
            print(f.read())
            print("Details read successfully")
            f.close()
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

import datetime
def getdate():
    import datetime
    return datetime.datetime.now()

def write(name, val):
    if name == 1:
        if val == 1:
            f = open("harry_food.txt", "a")
            print("Enter the food details")
            food_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(food_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        elif val == 2:
            f = open("harry_exercise.txt", "a")
            print("Enter the exercise details")
            exercise_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(exercise_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        else:
            print("Invalid Input")
    elif name == 2:
        if val == 1:
            f = open("akshay_food.txt", "a")
            print("Enter the food details")
            food_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(food_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        elif val == 2:
            f = open("akshay_exercise.txt", "a")
            print("Enter the exercise details")
            exercise_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(exercise_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        else:
            print("Invalid Input")
    elif name == 3:
        if val == 1:
            f = open("hammad_food.txt", "a")
            print("Enter the food details")
            food_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(food_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        elif val == 2:
            f = open("hammad_exercise.txt", "a")
            print("Enter the exercise details")
            exercise_det = input()
            f.write("[" + str(getdate()) + "]:  ")
            f.write(exercise_det)
            f.write("\n")
            print("Details Added Successfully")
            f.close()
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

if inp == 1:
    retrive(name, val)
elif inp == 2:
    write(name, val)
else:
    print("Invalid Input")
