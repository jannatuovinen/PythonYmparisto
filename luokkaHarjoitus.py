# Kokeillaan luokkia ja olioita

# LUOKKIA

# Yliluokka (Parent class, mother class, superclass)
class Henkilo:

    # Konstruktori(metodi), jonka avulla luodaan uusi Henkilö-olio
    # Oliota luotaessa etunimi ja sukunimi ovat pakollisia tietoja
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

        # Oliolla on myös muita ominaisuuksia, joita ei määritellä olion luomisen yhteydessä
        self.ika = 0 # Oletusikä 0
        self.kaupunki = '' # Asuinkaupunki tyhjä
        self.harrastukset = [] # Harrastukset tyhjä lista

# Aliluokka (Child class, daughter class subclass) perii (inherit) Henkilo-luokan 
class Opiskelija(Henkilo):

    # Oliota luotaessa pakollisia ovat etunimi ja sukunimi (koska pakollisia)
    # yliluokassa Henkilö sekä ryhmä
    # Metodi, joka muodostaa opiskelija-olion
    def __init__(self, etunimi, sukunimi, ryhma): # Olion muodostusmetodi
        super().__init__(etunimi, sukunimi) # Kertoo, että yliluokassa on määritelty etunimen ja sukunimen käsittely
        self.ryhma = ryhma # 

# Aliluokka (Child class, daughter class subclass) perii (inherit) Henkilo-luokan
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, aine):
        super().__init__(etunimi, sukunimi)
        self.aine = aine

# Aliluokka (Child class, daughter class subclass) perii (inherit) Henkilo-luokan
class Oppivelvollinen(Opiskelija):
    def __init__(self, etunimi, sukunimi, ryhma, paattyy):
        super().__init__(etunimi, sukunimi, ryhma)
        self.paattyy = paattyy

if __name__ == "__main__":

    # Johdetaan (instantiate) luokasta Henkilo olio rehtori
    rehtori = Henkilo('Reijo', 'Rantanen')
    rehtori.harrastukset = ['sulkapallo', 'rullaluistelu']

    # Luodaan olio opiskelija
    opiskelija = Opiskelija('Jakke', 'Jäynä', 'Tivi20oA')
    opiskelija.harrastukset = ['kokkaaminen', 'punttisali']

    # Luodaan olio Oppivelvollinen-luokasta
    oppivelvollinen = Oppivelvollinen('Jonne', 'Janttari', 'Tivi24A', '2027-05-20')
    oppivelvollinen.harrastukset = ['Pelaaminen', 'Velttoilu']
    print('Koulun rehtorina toimii', rehtori)

    print('Koulun rehtorina toimii', rehtori.etunimi, rehtori.sukunimi)

    print('Rehtori harrastaa', rehtori.harrastukset)

    print('Jakke Jäynä harrastaa', opiskelija.harrastukset)

    print('Jonne harrastaa', oppivelvollinen.harrastukset)