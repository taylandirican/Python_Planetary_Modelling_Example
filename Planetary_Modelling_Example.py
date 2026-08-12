class GökCismi:
    def __init__(self, Adi, Kütle, Hacim, Hız, YarıÇap):
        self.Adi = Adi
        self.Kütle = Kütle
        self.Hacim = Hacim
        self.Hız = Hız
        self.YarıÇap = YarıÇap

    def __str__(self):
        return f"Gezegenin Adı: {self.Adi}\nGezegenin Kütlesi: {self.Kütle}\nGezegenin Hacmi: {self.Hacim}\nGezegenin Hızı: {self.Hız}\nGezegenin Yarıçapı: {self.YarıÇap}"

    def KütleÇekimKuvveti(self, DiğerKütle, CisimlerinUzaklıkları):
        DiğerKütle = int(input("Diğer cismin kütlesini giriniz(kg): "))
        G = 6, 67
        return G * self.Kütle * DiğerKütle / CisimlerinUzaklıkları**2

    def YerÇekimiİvmesiYüzey(self):
        G = 6, 67
        return G * self.Kütle / self.YarıÇap**2
