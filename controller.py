from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def get_Nmax(self):
        return self._model.Nmax
    # creo funzione @property per poter accedere a Nmax, per non usare _Nmax

    def get_Tmax(self):
        return self._model.Tmax

    def reset(self, e):
        self._model.reset() #resetto lo stato del gioco lato modello!
        self._view._txtT.value = self._model.T
        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina il numero che sto pensando.")
        )
        self._view.update()


    def play(self, e):
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Error, you must enter an integer."))
            self._view.update()
            return

        res = self._model.play(tentativo)

        if res == 0:
            """HO  VINTO"""
            self._view.lvOut.controls.append(
                ft.Text(f"YOU WON!!! \n The correct number was {tentativo}",
                        color ="green")
            )
            self._view.update()
            return

        elif res == 2:
            """NON HO PIU' VITE"""
            self._view.lvOut.controls.append(
                ft.Text(f"YOU'VE LOST! \nThe correct number was {self._model.segreto}", )
            )
            self._view.update()
            return

        elif res == -1:
            """SEGRETO < TENTATIVO"""
            self._view.lvOut.controls.append(
                ft.Text(f"Try again, the secret number is smaller than {tentativo}")
            )
            self._view.update()
            return

        else:
            """SEGRETO > TENTATIVO"""
            self._view.lvOut.controls.append(
                ft.Text(f"Try again, the secret number is greater than {tentativo}")
            )
            self._view.update()
            return


