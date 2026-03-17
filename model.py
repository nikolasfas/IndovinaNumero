import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax
        self._segreto = None

    def reset(self):
        self._segreto = random.randint(0, self._Nmax)
        self._T = self._Tmax
        print(self._segreto)

    def play(self, tentativo):
        """Questo mmetodo riceve come paramenntro un valore intero
        che sarà il tentativo del  giocatore, e lo confronta con il segreto
        : return :
        -1 se il segreto è più piccolo del tentivo
        0 se il tentivo  è uguale al segreto
        1 se il segreto è più grande del tentivo
        2 se non ho più tentativi disponibili
        """

        self._T -= 1

        if tentativo == self._segreto:
            """HO VINTO"""
            return 0

        if self._T == 0:
            """NON HO PIU' VITE per cui non posso più giocare"""
            return 2

        elif tentativo > self._segreto:
            """il tentativo è più GRANDE del segreto"""
            return -1
        elif tentativo < self._segreto:
            """il tentativo è più PICCOLO del segreto"""
            return 1

    @ property
    def Nmax(self):
        return self._Nmax
    @property
    def Tmax(self):
        return self._Tmax
    @ property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m  =  Model()
    m.reset()
    print(m.play(34))
    print(m.play(56))
    print(m.play(12))
    print(m.play(66))
    print(m.play(74))
    print(m.play(58))