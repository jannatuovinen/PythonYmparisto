# YKSIKKÖTESTIT MODUULILLE identityCheck.py

import identityCheck

# Viiden numeron opiskelijanumero on oikein
def test_opiskelijanumeroOk_5():
    assert identityCheck.opiskelijanumeroOk('12345') == True

# Kuuden numeron opiskelijanumero on oikein
def test_opiskelijanumeroOk_6():
    assert identityCheck.opiskelijanumeroOk('123456') == True
 
# Neljä numeroa -> väärin
def test_opiskelijanumeroOk_4():
    assert identityCheck.opiskelijanumeroOk('1234') == False
 
# Seitsemän numeroa -> väärin
def test_opiskelijanumeroOk_7():
    assert identityCheck.opiskelijanumeroOk('1234567') == False

# Joukossa kirjain -> väärin
def test_opiskelijanumeroOk_kirjain():
    assert identityCheck.opiskelijanumeroOk('123X45') == False

# Joukossa desimaalipiste -> väärin
def test_opiskelijanumeroOk_desimaali():
    assert identityCheck.opiskelijanumeroOk('12.45') == False

# Joukossa desimaalipilkku
def test_opiskelijanumeroOk_desimaali2():
    assert identityCheck.opiskelijanumeroOk('12,45') == False

# TDD-TESTAUSTA
# -------------


def test_checkHeTuOK():
    assert identityCheck.checkHeTu('130728-478N') == (0, 'OK')

def test_checkHeTuShort():
    assert identityCheck.checkHeTu('13028-478N') == (1, 'Henkilötunnus liian lyhyt')

# Henkilötunnuksessa pitää olla 11 merkkiä, merkkejä on liikaa
def test_checkHeTuLong():
    assert identityCheck.checkHeTu('1307288-478N') == (2, 'Henkilötunnus liian pitkä')

# Henkilötunnuksen päiväosassa saa olla 01 - 31
def test_checkHeTuDays():
    assert identityCheck.checkHeTu('450728-478N') == (3, 'Päivä virheellinen')

# Henkilötunnuksen kuukausiosassa saa olla 01 - 12
def test_checkHeTuMonths():
    assert identityCheck.checkHeTu('132728-478N') == (4, 'Kuukausi virheellinen')

# Henkilötunnuksen vuosiosassa saa olla 00 - 99
def test_checkHetuYears():
    assert identityCheck.checkHeTu('13072x-478N') == (5, 'Vuosi virheellinen')

# Käytössä olevat vuosisatakoodit + (1800), - (1900) ja A (2000)
def test_checkHetuCenturyCode():
    assert identityCheck.checkHeTu('130728s478N') == (6, 'Vuosisatakoodi virheellinen')

# Henkilötunnuksen numeroista tehdään luku, esim. 130728478 ja jaetaan se luvulla 31. Jakojäännös on tarkiste. Jos on alle 10, käytetään numeroa, jos yli haetaan taulukosta vastaava kirjanmerkki 10 -> A, 11-> B. G ja I eivät ole käytössä.
def test_checkHeTuModulo():
    assert identityCheck.checkHeTu('130728-478M') == (7, 'Varmistussumma ei täsmää')