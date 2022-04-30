from Package.Heroj import Carobnjak, Oruzje, Macevalac
from Package.Cudoviste import Zmaj, Pauk
import random, logging

logging.basicConfig(filename="/home/mihailo/Desktop/game2/battle.log", level=logging.INFO)


mac = Oruzje('Mac', 10)
koplje = Oruzje('Koplje', 15)
carolija = Oruzje('Carolija', 20)

ranac1 = ['Carolija', 'Carolija']
ranac2 = ['Mac', 'Koplje']

carobnjak1 = Carobnjak(carolija, ranac1)
macevalac1 = Macevalac(mac, ranac2)

zmaj1 = Zmaj()
pauk1 = Pauk()

while True:
    c = random.randint(1, 100)
    if macevalac1.health <= 0:
        logging.info("Zmaj je pobedio")
        break
    
    if zmaj1.health <= 0:
        logging.info("Macevalac je pobedio.")
        break

    if c > 50:
        macevalac1.napad(zmaj1)
        logging.info(f"Macevalac je napao zmaja sa {macevalac1.weapon_in_hand.name} i skinuo mu {macevalac1.weapon_in_hand.damage} helta")
        logging.info(f"Zmajevi helti: {zmaj1.health}")
    else:
        napad = zmaj1.generisi_napad()
        zmaj1.napad(macevalac1, napad)
        logging.info(f"Zmaj je napao macevaoca sa {napad['type']} i skinuo mu {napad['damage']} helta")
        logging.info(f"Macevalac helti: {macevalac1.health}")

