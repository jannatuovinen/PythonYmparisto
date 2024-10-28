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


while True:
   
    userGivensSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivensSsn = userGivensSsn.upper() # Varmistetaan, että tarkiste on isolla
   
    # TODO; Tee tarkistus siitä, että nimi ei voi olla tyhjä
    
    # TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille -> reg exp
   

    
    
    ssnToCheck = identityCheck2.NationalSSN(userGivensSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastName = input('Syötä asikkaan sukunimi: ')
            userGivenLastName = userGivenLastName.capitalize()
            userGivenFirstName = input('Syötä asikkaan etunimi: ')
            userGivenFirstName = userGivenFirstName.capitalize()
            print('Asiakas:', userGivenLastName, userGivenFirstName)
            print('Syntymäaika', ssnToCheck.dateOfBirth)
            print('Ikä:', age)
            print('Sukupuoli:', ssnToCheck.gender)
        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe', e)
        

    # Kysy halutaanko poistua ohjelmasta
    wantAbort = input('Haluatko päättää ohjelman k/E: ')
    # Muutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko vastaus K
    if wantAbort.upper() == 'K':
        break # Poistutaan ikuisesta silmukasta

