# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# -----------------------------------

# KIRJASTOT JA MODUULIT
# ---------------------

# LUOKAT
# ------

# Hemkilötunnuksen käsittely
class NationalSSN:
    """Various methods to access and validate Finnish Social Security Number propersties
    """
    def __init__(self, ssn: str) -> None:
        """Generates a Finnish SNN object

        Args:
            ssn (str): 11 character SSN to process
        """
        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodit eri osien laskentaan ja järkevyystarkistuksiin

    # Tarkistetaan, että HeTu:n pituus on 11 merkkiä
    def checkSsnLengthOk(self) -> bool:
        """Checks correct length of the SSN

        Returns:
            bool: True if 11 chr othervise
        """
        ssnLength = len(self.ssn)
        if ssnLength !=11:
            return False
            # TODO: Mieti pitäisikö tässä generoida virheilmoitus (raise)
        else:
            return True

    # Pilkotaan henkilötunnus osiin
    def splitSsn(self) -> dict:
        """splits the SSN to functional parts ie. birthdate, century, number and the checksum

        Returns:
            dict: parts as strings
        """
        # Tehdään pilkkominen vain jos pituus on oikein
        if self.checkSsnLengthOk(): # Jos True pilkotaan, huom. self.metodin nimi
            dayPart = self.ssn[0:2]
            monthPart = self.ssn[2:4]
            yearPart = self.ssn[4:6]
            centuryPart = self.ssn[6]
            birthNumberPart = self.ssn[7:10]
            checksumPart = self.ssn[10]
            return {'days' : dayPart,
                    'months' : monthPart,
                    'years': yearPart,
                    'century': centuryPart,
                    'number': birthNumberPart,
                    'checksum': checksumPart
                    }
        else:
            # TODO: Mieti, pitäisikö synnyttää virhetilanne raisella
            return {'status' : 'error'}

    # Muutetaan syntymäaikaosa ja vuosisata päivämääräksi
    def getDateOfBirth(self, arg):
        pass

    # Lasktaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass

    # Selvitetään varmistussumman avulla onko HeTu syötetty oikein
    def isValid(self, arg):
        pass

# MAINKOKEILUJA VARTEN (Poista, kun ei enää tarvita)
# ==================================================

if __name__ == "__main__":
    hetu1 = NationalSSN('130728-478N')
    print('Oikein muodostettu:', hetu1.checkSsnLengthOk())
    print('HeTu:n osat ovat: ', hetu1.splitSsn())