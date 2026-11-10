class termometro:

    def __init__(self):
        self.temperatura = 0.0

    def marcar(self, valor):
        self.temperatura = valor

    def a_fahrenheit(self):
       return self.temperatura * 9/5 + 32

    def estado(self):
        if self.temperatura <= 0:
            print("esta congelado")
        elif self.temperatura <= 30:
            print("Esta templado")
        else:
            print("Calor extremo") 

sensor = termometro()
sensor.marcar(22.5)
print(f"{sensor.temperatura}°C equivalen a {sensor.a_fahrenheit():.1f}°F")  
sensor.estado()