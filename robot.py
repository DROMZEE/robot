# from robot import Robot

class Robot():

    def __init__(self, nom, x=0, y=0, direction='E'):
        self.nom = nom
        self.x = x
        self.y = y
        self.direction = direction

    def droite(self):
        #Nord
        if self.direction == "N":
            self.direction = "E"
        #Est
        elif self.direction == "E":
            self.direction = "S"
        #Sud
        elif self.direction == "S":
            self.direction = "O"
        #Ouest
        elif self.direction == "O":
            self.direction = "N"

    def position(self):
        position = self.x, self.y
        return position

    def etat(self):
        print("nom", self.nom, " x = ", self.x, " y = ", self.y, " Direction = ", self.direction)

    def avance(self):
        #Nord
        if self.direction == "N":
            self.y += 1
        #Est
        elif self.direction == "E":
            self.x += 1
        #Sud
        elif self.direction == "S":
            self.y -= 1
        #Ouest
        elif self.direction == "O":
            self.x -= 1
        else:
            pass

    print("Veuillez saisir un nom pour votre robot : ")
    #print("Saisir une direction : 'E' pour l'est, 'S' pour sud, 'O' pour ouest ou 'N' pour nord")