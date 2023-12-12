x = input("zadej promenou x: ")
y = input("zadej promenou y: ")

x = int(x)
y = int(y)

print("zde mate moznosti")
print("pro sčítání zadej +")
print("odcitani zadej -")
print("nasobeni zadej *")
print("deleni zadej /")
print("pro mocněni zadej **, x = mocnenec a y = mocnitel ")
print("pro odmocneni zadej odm, x = odmocněnec a y = odmocnitel")

znamenko = input("vyber operaci")

if znamenko == "+":
    print(x+y)
elif znamenko == "-":
    print(x-y)
elif znamenko == "/":
    if y == 0:
        print("nelze delit noluo")
    else:
        print(x/y)
elif znamenko == "*":
    print(x*y)
elif znamenko == "**":
    print(x**y)
elif znamenko == "odm":
    print(x**(1/2)y)
    if y == 0:
        print("nelze odmocnit 0")
    else:
        print(x**(1/2)y)
