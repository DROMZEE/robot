from robot import Robot

class RobotNG(Robot):
    def __init__(self, nom, x=0, y=0, direction='E', turbo=False):
        self.__turbo = turbo
        super().__init__(nom, x=0, y=0, direction='E')

    def avance(self,pas=2):
        if self.__turbo==True:
            pas = pas * 3
        for i in range(pas):
            super().avance()

    def demiTour(self):
        self.droite()
        self.droite()

    def gauche(self):
        self.droite()
        self.droite()
        self.droite()

    def etat(self):
        if self.__turbo==True:
            print("le robot est en mode turbo")
        super().etat()