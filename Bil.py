class Bil:
    def __init__(self):
        self.registreringsnummer = ''
        self.fabrikat = '' 
        self.årsmodell = ''
        self.tjänstevikt = ''
        self.motoreffekt = ''
        self.färg = ''
        self.ägare = None

class Person:
    def __init__(self):
        self.namn = ''
        self.ålder = ''

person_1 = Person()
person_1.namn = 'Erik'
person_1.ålder = '26'

person_2 = Person()
person_2.namn = 'Tobias'
person_2.ålder = '40'

person_3 = Person()
person_3.namn = 'Alice'
person_3.ålder = '19'

bil_1 = Bil()
bil_1.registreringsnummer = 'NOJ01B'
bil_1.fabrikat = 'Volvo v60'
bil_1.årsmodell = '2020'
bil_1.tjänstevikt = '1 891 kg'
bil_1.motoreffekt = '190 hk / 140kW'
bil_1.färg = 'röd'
bil_1.ägare = person_1

bil_2 = Bil()
bil_2.registreringsnummer = 'RJP05G'
bil_2.fabrikat = 'Volvo v60'
bil_2.årsmodell = '2020'
bil_2.tjänstevikt = '1 750 kg'
bil_2.motoreffekt = '190 hk / 140kW'
bil_2.färg = 'blå'
bil_2.ägare = person_2

bil_3 = Bil()
bil_3.registreringsnummer = 'RJP05G'
bil_3.fabrikat = 'Volvo v60'
bil_3.årsmodell = '2020'
bil_3.tjänstevikt = '1 689 kg'
bil_3.motoreffekt = '190 hk / 140kW'
bil_3.färg = 'gul'
bil_3.ägare = person_3

bil_4 = Bil()
bil_4.registreringsnummer = 'RJP05G'
bil_4.fabrikat = 'Volvo v60'
bil_4.årsmodell = '2020'
bil_4.tjänstevikt = '1 703 kg'
bil_4.motoreffekt = '190 hk / 140kW'
bil_4.färg = 'rosa'
bil_4.ägare = person_3

bilar = [bil_1, bil_2, bil_3, bil_4]

for bil in bilar:
    print("")
    print(f"registreringsnummer: {bil.registreringsnummer}")
    print(f"fabrikat: {bil.fabrikat}")
    print(f"årsmodell: {bil.årsmodell}") 
    print(f"tjänstevikt: {bil.tjänstevikt}") 
    print(f"motoreffekt: {bil.motoreffekt}")
    print(f"färg: {bil.färg}")
    print(f"ägare: {bil.ägare.namn}")
    print("")
