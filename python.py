print("1. for simple interest")
print("2. for compound interest")

ch = input("enter choice")

if ch == "1":
    p = 100
    t = 12
    r = 2

    si = p * (1 + (r * t))

    print('The Simple Interest is', si)

elif ch == "2":
    p = 100
    t = 12
    r = 2
    CI = p * (1 + r / 100) * t
    print("Compound interest is", CI)

else:
    print("Wrong Choice!")