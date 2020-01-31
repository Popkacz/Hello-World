Weight = input("What's your weight? ")
Medida = input("(L)bs or (K)g? ")

if Medida.upper() == "L":
    print(f"You are {int(Weight) * 0.45} Kgs")
elif Medida.upper() == "K":
    print(f"You are {int(Weight) * 2.2} Lbs")



