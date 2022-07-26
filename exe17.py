from math import hypot, sqrt


co=float(input("co\n"))
ca=float(input("\nca\n"))

hip=sqrt(co**2 + ca**2)
print("a hipotenusa é:", hypot(co, ca))