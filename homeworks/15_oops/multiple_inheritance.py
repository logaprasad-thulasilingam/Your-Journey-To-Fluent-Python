class Phone:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    def call(self):
        return f"Calling from {self.number} with {self.brand}"

class Camera:
    def __init__(self, mps):
        self.mps = mps

    def take_photo(self):
        return f"Taking photo with {self.mps} megapixels camera"

class Smartphone(Phone, Camera):
    def __init__(self,brand,number,mps):
        Phone.__init__(self,brand,number)
        Camera.__init__(self,mps)

sp = Smartphone(brand= 'Iphone', number=123456789, mps=45)

print(sp.call())
print(sp.take_photo())