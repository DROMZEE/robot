# Le nom, la position et la direction d'un robot lui sont donnés au moment de sa création. 
# Le nom est obligatoire mais 
# on peut ne pas spécifier la position et la direction, qui sont définis par défaut à (0,0) et “Est”.

from robot import Robot
from robotng import RobotNG

ivanka = Robot("Ivanka")

ivanka.etat()
ivanka.avance()
ivanka.droite()
ivanka.avance()
ivanka.etat()
ivanka.droite()
ivanka.avance()
ivanka.etat()
ivanka.droite()
ivanka.avance()
ivanka.etat()
ivanka.droite()
ivanka.avance()
ivanka.avance()
ivanka.avance()
ivanka.avance()
ivanka.etat()

# Test 2 avec parametres de position et de direction a la creation
# « R2D2 » et « C3PO » de Star Wars (1977)

c3po = Robot("C3PO", x=2, y=3, direction='N')

c3po.etat()
c3po.droite()
c3po.droite()
c3po.avance()
c3po.etat()

#test 3 RobotNG avec gauche()
# Le T-800«  de Terminator (1984)

t800 = RobotNG("T-800", x=1, y=1, direction='O')

t800.etat()
t800.droite()
t800.avance()
t800.etat()
t800.gauche()
t800.avance()
t800.etat()

#test 4 avec turbo (Maria - Metropolis 1927)

maria = RobotNG("Maria", x=1, y=1, direction='O')

maria.etat()
maria.droite()
maria.avance()
maria.etat()
maria.gauche()
maria.avance(pas=4)
maria.etat()

#test 5 RobotNG avec pas=4
#HAL 9000 (CARL 500 en version française) supercalculateur & IA dans  2001, l'Odyssée de l'espace (1968) de Stanley Kubrick 

hal9000 = RobotNG("HAL 9000", x=1, y=1, direction='O')

hal9000.etat()
hal9000.droite()
hal9000.avance()
hal9000.etat()
hal9000.gauche()
hal9000.avance(pas=4)
hal9000.etat()

#test 6 RobotNG avec pas=4 et turbo
#meidi_a_14h

meidi = RobotNG("Meidi à 14h", turbo=True)

meidi.etat()
meidi.droite()
meidi.avance()
meidi.etat()
meidi.gauche()
meidi.avance(pas=4)
meidi.etat()