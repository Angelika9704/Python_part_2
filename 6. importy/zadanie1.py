import main1
from main1 import dodawanie
from main1 import odejmowanie
from main1 import dzielenie
from main1 import mnozenie

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