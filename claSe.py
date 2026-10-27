class auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.habilitados = []
        self.no_habilitados = []

    def getInfo(self):
        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("Año: ", self.año)

    def getConductores(self):
        if self.habilitados:
            print("Conductores habilitados del auto")
            for i in self.habilitados:
                print ("-", i)
        else:
            print("No hay conductores habilitados registrados por este auto")
        if self.no_habilitados:
            print("conductores no habilitados del auto:")
            for i in self.no_habilitados:
                print("-", i)

    def setConductor(self, conductor):
        self.habilitados.append(conductor)

    def setNoHablitados(self, noconductor):
        self.no_habilitados.append(noconductor)