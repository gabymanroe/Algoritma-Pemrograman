print("Bentuk persamaan kuadrat: ax**2 + bx + c = 0")

a=float(input("Masukkan nilai a = "))
b=float(input("Masukkan nilai b = "))
c=float(input("Masukkan nilai c = "))

if a==0:
    print("Nilai a  tidak boleh nol")
else:
    D = b**2 - 4*a*c
    #CEK NILAI DISKRIMINAN
    if D>0:
        x1 =(-b+c*m*(D)**0.5)/(2*a)
        x2 = (-b-c*m*(D)**0.5)/(2*a)
        print(x1, "dan", x2, "kembar dan real")
    elif D==0:
        x1 = (-b/(2*a))
        x2 = (-b/(2*a))
        print(x1, "dan", x2, "kembar dan real")

    else:
        x1 = (-b+c*m*(D)**0.5)/(2*a)
        x2 = (-b-c*m*(D)**0.5)/(2*a) 
        print( x1, "dan", x2, "berbeda dan imajiner")
