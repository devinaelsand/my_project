#
# Devina
# Calculator
#

sum = 0

while True:
    # 1. Input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters   : "))

    # 2. Process
    BMI = weight/ (height*height)

    # 3. Output
    print("Your BMI is:", BMI)
    option = input("Do you want to continue? (yes/no):")
    if option == 'yes':
        continue
    else:
        break
    