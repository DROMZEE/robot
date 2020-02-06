# Le nom, la position et la direction d'un robot lui sont donnés au moment de sa création. 
# Le nom est obligatoire mais 
# on peut ne pas spécifier la position et la direction, qui sont définis par défaut à (0,0) et “Est”.

from robot import Robot

robot1 = Robot("Ivanna")

robot1.etat()
robot1.avance()
robot1.droite()
robot1.avance()
robot1.etat()
robot1.droite()
robot1.avance()
robot1.etat()
robot1.droite()
robot1.avance()
robot1.etat()
robot1.droite()
robot1.avance()
robot1.avance()
robot1.avance()
robot1.avance()
robot1.etat()

# Test 2

c3po = Robot("C3PO", x=2, y=3, direction='N')

c3po.etat()
c3po.droite()
c3po.droite()
c3po.avance()
c3po.etat()