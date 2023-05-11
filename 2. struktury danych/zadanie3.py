lista = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
litera = input("Podaj literę: ")
for element in lista:
    if element.startswitch(litera):
        print(element, end=" ")