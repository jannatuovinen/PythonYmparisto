class Hemmo:
    """Yliluokka, jossa ei ole yhtään pakollista parametriä"""
    def __init__(self, etunimi, sukunimi):
        self.etunimi = ''
        self.sukunimi = ''
        self.harrastukset = []

class Stara(Hemmo):
    """Aliluokka, joka perii Hemmo-luokan ominaisuudet"""
    def __init__(self, etunimi, sukunimi,soitin):
        super.__init__(etunimi,sukunimi)

        self.soitin = soitin

if __name__ == "__main__":
    hemmo1 = Hemmo('Ilkka', 'Lipsanen')
    hemmo2 = Hemmo('Martti', 'Syrjä')
    stara1 = Stara('Garry', 'Glitter', 'Laulu')

    hemmo1.etunimi = 'Heikki'
    hemmo1.sukunimi = 'Harma'
    hemmo1.harrastukset = ['Laulaminen', 'Kitaran soitto']

    print('Ja tämä hemmo on', hemmo1.etunimi, hemmo1.sukunimi, 'joka harrastaa', hemmo1.harrastukset)
    print(stara1.etunimi, stara1.sukunimi, 'oli suosittu 1970-luvulla')