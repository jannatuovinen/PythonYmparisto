# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkkimoduuli
# from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# TODO: Pääohjelman ikuinen silmukka, josta poistutaan tarvittaessa (keksi menismi itse)
# TODO: Paranna pääohjelmaa siten, että se ei kaadu, kun käyttäjä syöttää virheellisen henkilötunnuksen
userGivensSsn = input('Syötä asiakkaan henkilötunnus: ')
userGivenLastName = input('Syötä asikkaan sukunimi')
# Tee tarkistus siitä, että nimi ei voi olla tyhjä
userGivenFirstName = input('Syötä asikkaan etunimi')
# TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
# TODO: Varaudu toöamteeseen, jossa hetu:n tarkiste on annettu pienillä kirjaimilla
# TODO: Muuta syötetty nimien alkukirjain isoksi

ssnToCheck = identityCheck2.NationalSSN(userGivensSsn)
if ssnToCheck.isValidSsn() == True:
    dateOfBirth = ssnToCheck.getDateOfBirth
    gender = ssnToCheck.getGender()
    age = ssnToCheck.calculateAge()
    print('Syntymäaika', ssnToCheck.dateOfBirth)
    print('Ikä:', age)
    print('Sukupuoli:', ssnToCheck.gender)

