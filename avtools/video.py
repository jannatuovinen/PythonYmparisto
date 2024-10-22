# MODUULI VIDEOKUVAN KÄSITTELYYN
# ==============================

# KIRJASTOT JA MODUULIT
# ---------------------

# Ulkoinen kirjasto opencv-python ladataan nimellä cv2
import cv2

# FUNKTIO, JOKA KÄYNNISTÄÄ WEB-KAMERAN JA NÄYTTÄÄ KUVAA IKKUNASSA
# ---------------------------------------------------------------

def webstream(camIx):
    """Opens videostream and shows frames in window
    Args:
        camix (int): Index of the camera starting from 0
    """

    # Määritellään kameraikkunan nimi
    windowName = "Kamera " + str(camIx)

    # Luodaan videostriimi
    capture = cv2.VideoCapture(camIx)
    
    # IKUINEN SILMUKKA KAMERALLE
    # ============================

    # Näytetään videokuvaa niin kauan, kuin sitä tulee
    while capture.isOpened():
        ret, frame = capture.read()
        
        # Kun striimi loppuu, poistutaan silmukasta
        if not ret:
            print("Can't receive frames. Exiting ...")
            break
    
        # Määritellään poistumisnäppäin q
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    # Vapautetaan lopuksi muisti ja tuhotaan ikkuna
    capture.release()
    cv2.destroyAllWindows()

    # TESTIT
    # ======
    if __name__ == "__main__":
        webstream(1)