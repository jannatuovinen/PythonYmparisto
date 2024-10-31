# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
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
        question = question + ': '
        name = input(question).strip()
    name = name.title()
    return name



# Varmistetaan, ettei ohjelma käynnisty, kun se tuodaan toiseen moduuliin importilla

if __name__ == "__main__":

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
        
   

    
    
        # Luodaan syötetystä henkilötunnuksesta NationalSSN-objekti
        ssnToCheck = identityCheck2.NationalSSN(userGivensSsn)

        # Tarkistetaan onko henkilötunnus oikein muodostettu
        if ssnToCheck.isValidSsn() == True:

            # Virheenkäsittely, mahdollisen vuosisatakoodivirheen varalta
            try:
                ssnToCheck.getDateOfBirth() # Asetetaan syntymäaika ominaisuus
                ssnToCheck.getGender() # Asetetaan sukupuoliominaisuus
                age = ssnToCheck.calculateAge() # Lasketaan ikä tänään

                # Kysytään loput tiedot, jos ei virhettä
                userGivenLastName = askName('Asiakkaan sukunimi')
                userGivenFirstName = askName('Asiakkaan etunimi')

                # Tulostetaan tiedot ruudulle
                print('Asiakas:', userGivenLastName, userGivenFirstName)
                print('Syntymäaika', ssnToCheck.dateOfBirth)
                print('Ikä:', age)
                print('Sukupuoli:', ssnToCheck.gender)
            
            # Virhetilanteessa näytetään virheilmoitus
            except Exception as e:
                print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe', e)
        
        else:
            print('Henkilötunnuksessa virhe, syötä tunnus uudelleen')

        # Kysy halutaanko poistua ohjelmasta
        wantToAbort = input('Haluatko päättää ohjelman k/E: ')
        # Muutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko vastaus K
        if wantToAbort.upper() == 'K':
            break # Poistutaan ikuisesta silmukasta