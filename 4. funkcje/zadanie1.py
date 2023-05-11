# Funkcje wykonujące podstawowe operacje matematyczne
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

# Pętla główna programu
while True:
    # Pytamy użytkownika, jaką operację chce wykonać
    print("Wybierz operację, którą chcesz wykonać:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("0. Wyjście")
    
    # Pobieramy wybór użytkownika
    wybor = input("Wybierz opcję (0-4): ")
    
    # Obsługujemy wybór użytkownika
    if wybor == "0":
        break
    elif wybor == "1":
        # Dodawanie
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = dodawanie(a, b)
        print(f"Wynik: {wynik}")
    elif wybor == "2":
        # Odejmowanie
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = odejmowanie(a, b)
        print(f"Wynik: {wynik}")
    elif wybor == "3":
        # Mnożenie
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = mnozenie(a, b)
        print(f"Wynik: {wynik}")
    elif wybor == "4":
        # Dzielenie
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        try:
            wynik = dzielenie(a, b)
            print(f"Wynik: {wynik}")
        except ValueError as e:
            print(e)
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
