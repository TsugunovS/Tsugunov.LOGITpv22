from math import * 

print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\ läbimõõduga {C} ümbermõõt võrdub {d}")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")

