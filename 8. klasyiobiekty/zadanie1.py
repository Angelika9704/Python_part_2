class Czytelnik:
    id: int = -1

    def __init__(self,
                 czytelnik_imię:str, czytelnik_nazwisko:str, czytelnik_wiek:int, czytelnik_nr_tel:int):
        Czytelnik.id += 1
        self.__id = Czytelnik.id
        self.__czytelnik = self.stworz_czytelnik(czytelnik_imię, czytelnik_nazwisko)
        self.__wiek = czytelnik_wiek
        self.__tel = czytelnik_nr_tel
    
    def stworz_czytelnik(self, imie: str, nazwisko: str) -> "dict[str, str]":
        return {"imie": imie, "nazwisko": nazwisko}

    def pobierz_id(self) -> int:
        return self.__id
    def pobierz_czytelnik(self) -> "dict[str, str]":
        return self.__czytelnik
    def pobierz_wiek(self) -> int:
        return self.__wiek
    def pobierz_tel(self) -> int:
        return self.__tel