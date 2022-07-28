# Find student grade (Operators, DM, Loops with CS)

marks = int(input("Enter marks :"))

# Validation
if marks >= 0 and marks <= 100:
    print("---Valid marks---")
    if marks >= 35:
        print("-- RESULT : PASS --")
        if marks >= 60 and marks <= 100:
            print("- First Class -")
            if marks == 100:
                print("** Distinction **")
        elif marks >= 50 and marks < 60:
            print("- Second Class -")
        else:   # 35 - 50
            print("- Third Class - ")
    else:
        print("-- RESULT : FAIL --")
else:
    print("---Invalid marks---")


'''
if marks >= 0 and marks <= 100:
    print("-----Valid marks -------")
    if marks >= 35:
        print("RESULT  ---> PASS")
        if marks >= 60:
            print("***First Class***")
            if marks == 100:
                print("--Congratulations--")
            elif marks >= 90:
                print("---Good------------")
        elif marks >= 50 and marks < 60:
            print("***Second Class***")
        else:
            print("***Third Class***")

    else:  # elif marks < 35
        print("RESULT  ---->FAIL")
else:
    print("----Invalid marks--------")
'''