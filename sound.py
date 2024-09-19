# MODUULI ÄÄNIMERKKIEN ANTAMISEEN
# ===============================

# KIRSJASTOT JA MODUULIT
# ======================

# Windows-äänet
import winsound

# Ajankäsittely
import time

# ÄÄNIFUNKTIOT
# ============

def shortBeep():
    """Creates a 1 kH< sound for 1/4 second
    """
    winsound.Beep(1000, 250)

def longbeep():
    """Creates a 1 kH< sound for 2 second
    """
    winsound.Beep(1000,2000)

def waitMs(ms):
    """Waits for a timeperiod

    Args:
        ms (int): time in milliseconds
    """
    seconds = ms / 1000
    time.sleep(seconds)

    # Säädettävät äänet 1. korkeus ja kesto parametreina
    def parametricBeep(frequency, duration=250):
        """Produces a sound at given frequency and duration

        Args:
            frequency (int): Frequency of the tone in Hz
            duration (int): Durantion in milloseconds
        """
        winsound.Beep(frequency, duration)

    # Säädettävät äänet 2. toistuva äänimerkki korkeus, kesto ja määrä
    def repeatingBeep(frequency: int, duration: int, count: int) -> None:
        """Creates a repeating buzzer sound

        Args:
            frequency (int): Tone frequency in Hz
            duration (int): Duration of the single tone in milliseconds
            count (int): How many times sound will be repeated
        """
        for i in range(count):
            winsound.Beep(frequency, duration)
            waitMs(250)

    # Ääni tulee halutusta tiedostosta, parametrina äänen nimi

    def playWav(FileName: str) -> None:
        """Plays a wav file

        Args:
            FileName (str): Name of the audiofile
        """
        winsound.PlaySound(FileName, winsound.SND_FILENAME)

    if __name__ == "__main__":
        # shortBeep()
        # waitMs(500)
        # longbeep()
        # waitMs(500)
        # parametricBeep(360)
        repeatingBeep(360, 500, 5)
        waitMs(1000)
        playWav("Alkaa.WAV")
        waitMs(1000)
        playWav("Loppuu.WAV")