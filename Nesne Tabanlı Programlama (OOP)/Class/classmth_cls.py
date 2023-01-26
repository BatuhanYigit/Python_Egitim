class Sinif():
    sinif_niteligi = 0

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.ornek_niteligi = 0

    def ornek_metodu(self):
        self.ornek_niteligi += 1
        return self.ornek_niteligi
    @classmethod
    def sinif_metodu(cls):
        cls.sinif_niteligi += 1
        return cls.sinif_niteligi