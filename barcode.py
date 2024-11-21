# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKTIOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generatiom

    Args:
        character (str): a single character to convert

    Returns:
        int: Code128B value for calculating the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculateCode128BChecksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: Modulo 103 checksum weighted values
    """
    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum = weightedSum + weightedValue
    weightedSum = weightedSum + 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum


def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code 128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BarcodeString = ''
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculateCode128BChecksum(text)
    checkSumSymbol = chr(checkSum + 32)
    code128BarcodeString = startChar + text + checkSumSymbol + stopChar
    return code128BarcodeString

# LUOKKA VIIVAKOODEILLE
# =====================

class Code128B():
    """Generates Code128B barcodes. Supports variants common, uncommon and Barcodesoft"""
    def __init__(self, text: str, variant: str = 'Common') -> None:
        """Checks if text contains only valid characters for Code128B barcode

        Args:
            text (str): A text string to be converted into a barcode
            variant (str, optional): Variant of Code128B. Valid values: Common, Uncommon, and Barcodesoft. Defaults to 'Common'.
        """
        self.text = text
        self.variant = variant
        self.validRangeAll = range(33,126)
        self.validRangeCommon = range(195,202)
        self.valisRangeUncommon = range(200,207)
        self.validRangeBarcodesoft = range(240,247)
        self.commonSpecialChar =(32, 194, 207)
        self.uncommonSpecialChar = 212
        self.barcodeSoftSpecialChar = 252


    def checkValidityOfText(self) -> bool | None:
        textLenght = len(self.text)
        isValid = False
        if self.variant == 'Common':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.validRangeCommon or characterValue in self.commonSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)
        
        elif self.variant == 'Uncommon':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.validRangeCommon or characterValue == self.uncommonSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)
                    
        elif self.variant == 'Barcodesoft':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.validRangeCommon or characterValue == self.uncommonSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)
                    
        else:
                errorMessage = 'Invalid variant ' + '(' + self.variant + '): Common, Uncommon and Barcodesoft supported'
                raise ValueError(errorMessage)
            
        return isValid

    # Metodi, joka tuottaa viivakoodin sisällön
    def buildBarcode(self) -> str:
        """Returns a string presentation of the barcode

        Returns:
            str: barcode with start symbol, text, checksum symbol and stop symbol
        """
        rawText = self.text
        variant = self.variant
        startValues = {'Common': 204, 'Uncommon': 209, 'Barcodesoft': 249}
        stopValues = {'Common': 206, 'Uncommon': 211, 'Barcodesoft': 251} 
        subtractValues = {'Common': 100, 'Uncommon': 105, 'Barcodesoft': 145}

        # Katsotaan onko tekstissä pelkästään sallittuja merkkejä
        if self.checkValidityOfText() == True:
            rawTextLenght = len(rawText)
            weightedSum = 0

            # Käydään merkkijonon silmukassa läpi ja lasketaan varmistussumman arvot
            for index in range(rawTextLenght):
                character = rawText[index]
                characterValue = ord(character)

                # Normaalit merkit 32 - 126, alle 32 ei tarvitse enää huomioida
                if characterValue < 127:
                    value = characterValue -32

                 # Erikoismerkit, joiden arvo on 0   
                elif characterValue in (194, 207, 212, 252):
                    value = 0

                # Varianttien erikoismerkit, rajat tarkisettu jo aiemmin   
                else:
                    value = characterValue - subtractValues[variant]


                # Kirjaimen painotetun arvon lisääminen, huom indeksi alkaa 0:sta kertoimet 1:sta 
                weightedSum = weightedSum + (index + 1) * value

            # Alkumerkin sisältävä painotettu summa
            weightedSum = weightedSum + startValues[variant]
            
            # Lopullinen vamistussumma jakojäännös 103:lla jaettaessa
            checksum = weightedSum % 103

            # Generoidaan lopullinen viivakoodi alkumerkki + raakateksti + varmistussumma + loppumerkki
            startChar = chr(startValues[variant])
            stopChar = chr(stopValues[variant])
            checksumChar = chr(checksum + 32)
            barcode = startChar + rawText + checksumChar + stopChar

        return barcode

          
if __name__ == "__main__":
    testi = Code128B('128B')
    try:
        tulos = testi.checkValidityOfText()
        print(testi.text, 'on kelvollinen viivakoodiksi', tulos)
        viivakoodi = testi. buildBarcode()
        print('Viivakoodin sisältö on', viivakoodi)
    except Exception as e:
        print('Tapahtui virhe', testi.text, e)