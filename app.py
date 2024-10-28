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

# FUNKTIOT
# --------

def askName(question: str) -> str:
    """Promts user to answer a question and converts the answers to title and removes white space

    Args:
        question (str): Promt to user

    Returns:
        str: modifies answer
    """
    name = ''
    while name == '':
        name = input(question).strip()
    name = name.title()
    return name

# PÄÄOHJELMAN IKUINEN SILMUKKA
# ============================
while True:

    # Alustetaan muuttujat tyhjiksi
    userGivensSsn = ''
    userGivenLastName = ''
    userGivenFirstName = ''
   
   # Kysytään asiakkaan henkilötunnus ja muutetaan kirjaimet isoksi
    userGivensSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivensSsn = userGivensSsn.upper() # Varmistetaan, että tarkiste on isolla
    
    # TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille -> .title()
   

    
    # Luodaan syötetystä henkilötunnuksesta NationalSSN-objekti
    ssnToCheck = identityCheck2.NationalSSN(userGivensSsn)

    # Tarkistetaan onko henkilötunnus oikein muodostettu
    if ssnToCheck.isValidSsn() == True:

        # Virheenkäsittely, mahdollisen vuosisatakoodivirheen varalta
        try:
            ssnToCheck.getDateOfBirth
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()

            # Kysytään loput tiedot, jos ei virhettä
            while userGivenLastName == '':
                userGivenLastName = input('Syötä asikkaan sukunimi: ')
            userGivenLastName = userGivenLastName.title()
            while userGivenFirstName == '':
                userGivenFirstName = input('Syötä asikkaan etunimi: ')
            userGivenFirstName = userGivenFirstName.title()

            # Tulostetaan tiedot ruudulle
            print('Asiakas:', userGivenLastName, userGivenFirstName)
            print('Syntymäaika', ssnToCheck.dateOfBirth)
            print('Ikä:', age)
            print('Sukupuoli:', ssnToCheck.gender)
        
        # Virhetilanteessa näytetään virheilmoitus
        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe', e)
        
    # TODO: Lisää tähän else-haara, joka kertoo, että HeTu oli virheellinen

    # Kysy halutaanko poistua ohjelmasta
    wantToAbort = input('Haluatko päättää ohjelman k/E: ')
    # Muutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko vastaus K
    if wantToAbort.upper() == 'K':
        break # Poistutaan ikuisesta silmukasta

if __name__ == "__main__":
    askName('Anna etunimi')

