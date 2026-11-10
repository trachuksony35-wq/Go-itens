"""Determine a point's quadrant and report a student's exam result."""

x = float(input("Введіть координату X:"))
y = float(input("Введіть координату Y:"))

# Check Y first, then use X to distinguish the quadrants.
if y > 0:
    if x > 0:
        print("Точка знаходиться у I чверті.")
    elif x < 0:
        print("Точка знаходиться у II чверті.")
    else:
        print("Точка знаходиться на додатній півосі Y.")
elif y < 0:
    if x > 0:
        print("Точка знаходиться у IV чверті.")
    elif x < 0:
        print("Точка знаходиться у III чверті.")
    else:
        print("Точка знаходиться на від'ємній півосі Y.")
elif x > 0:
    print("Точка знаходиться на додатній півосі X.")
elif x < 0:
    print("Точка знаходиться на від'ємній півосі X.")
else:
    print("Точка знаходиться у початку координат.")

surname = input("Введіть прізвище студента:")
score = int(input("Введіть кількість балів:"))

if score > 80:
    print(f"Студент{surname}склав іспит.")
else:
    print(f"Студент{surname}не склав іспит.")