# from robot import Robot

class Robot():

    def __init__(self, nom, x=0, y=0, direction='E'):
        self._nom = nom
        self._x = x
        self._y = y
        self._direction = direction

    def droite(self):
        #Nord
        if self._direction == "N":
            self._direction = "E"
        #Est
        elif self._direction == "E":
            self._direction = "S"
        #Sud
        elif self._direction == "S":
            self._direction = "O"
        #Ouest
        elif self._direction == "O":
            self._direction = "N"

    def position(self):
        position = self.x, self.y
        return position

    def etat(self):
        print("nom", self._nom, " x = ", self._x, " y = ", self._y, " Direction = ", self._direction)

    def avance(self):
        #Nord
        if self._direction == "N":
            self._y += 1
        #Est
        elif self._direction == "E":
            self._x += 1
        #Sud
        elif self._direction == "S":
            self._y -= 1
        #Ouest
        elif self._direction == "O":
            self._x -= 1
        else:
            pass

    print("Veuillez saisir un nom pour votre robot : ")