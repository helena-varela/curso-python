# 9.9 – Upgrade de bateria: Use a última versão de electric_car.py desta seção.
# Acrescente um método chamado upgrade_battery() na classe Battery. Esse
# método deve verificar a capacidade da bateria e defini-la com 85 se o valor for
# diferente. Crie um carro elétrico com uma capacidade de bateria default, chame
# get_range() uma vez e, em seguida, chame get_range() uma segunda vez após
# fazer um upgrade da bateria. Você deverá ver um aumento na distância que o
# carro é capaz de percorrer.

class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWhbattery.")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print(f'A bateria foi mudada para {self.battery_size}')
        else: print('A bateria já é 85 KWh')

class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """ Inicializa os atributos da classe pai Em seguida, inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWhbattery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
