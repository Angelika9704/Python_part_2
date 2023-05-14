from os import path
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)
with open(data_path, "r", encoding="utf-8") as f:
    file_lines = f.readlines()
    print(file_lines)
# zamień znaki interpunkcyjne na spacje
tekst = tekst.replace(",", " ")
tekst = tekst.replace(".", " ")
tekst = tekst.replace("!", " ")
tekst = tekst.replace("?", " ")

# podziel tekst na słowa
slowa = tekst.split()
# policz liczbę słów
liczba_slow = len(slowa)
print("Liczba słów w tekście: ", liczba_slow)

# przygotuj słownik z wynikami
statystyki = {}
for slowo in slowa:
    ostatnia_litera = slowo[-1].lower()
    if ostatnia_litera in statystyki:
        statystyki[ostatnia_litera] += 1
    else:
        statystyki[ostatnia_litera] = 1
# wyświetl statystyki
print("Statystyki końcówek słów:")
for litera, liczba_slow in statystyki.items():
    print(litera,":", liczba_slow, "słów")
