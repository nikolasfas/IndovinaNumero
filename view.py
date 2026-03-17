import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txtNmax = ft.TextField(label="MAX NUMBER",
                                     value=  self._controller.get_Nmax(),
                                     disabled=True)
        # la view e il modello non si devono parlare, in mezzo  sempre il controller

        self._txtTmax =  ft.TextField(label="MAX NUMBER OF TRIALS",
                                      value= self._controller.get_Tmax(),
                                      disabled=True)

        self._txtT = ft.TextField(label="REMAINING TRIALS",
                                 disabled=True)


        self.row1 = ft.Row(controls = [self._txtNmax, self._txtTmax, self._txtT ])
        # aggiunta + update degli oggetti grafici

        self._txtInTentativo = ft.TextField(label =  "valore")

        self._btnReset = ft.ElevatedButton(text="New game",
                                         on_click= self._controller.reset)

        self._btnPlay = ft.ElevatedButton(text="Guess the number",
                                        on_click= self._controller.play)

        self.row2 = ft.Row(controls = [self._txtInTentativo,
                                       self._btnReset,
                                       self._btnPlay])

        self.lvOut = ft.ListView(expand=True)

        self._page.add(self.row1, self.row2, self.lvOut)
        # self._page.update()


    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()