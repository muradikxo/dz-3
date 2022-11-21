class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    def __str__(self):
        return f"{self.__cpu}, {self.__memory}"

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.cpu = value


    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.memory = value

    
    def __add__(self, other):
        return self.cpu + other.memory

    def __sub__(self, other):
        return self.cpu - other.memory

    def __mul__(self, other):
        return self.cpu * other.memory

    def __floordiv__(self, other):
        return self.cpu // other.memory



    def __eq__(self, other):
        return f"{self.memory} == {other.memory}"

    def __lt__(self, other):
        return f"{self.memory} < {other.memory}"

    def __gt__(self, other):
        return f"{self.memory} > {other.memory}"

    def __le__(self, other):
        return f"{self.memory} <= {other.memory}"

    def __ge__(self, other):
        return f"{self.memory} >= {other.memory}"

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    def __str__(self):
        return f"{self.__sim_cards_list}"


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.sim_cards_list = value




    def Call(self,sim_card_number, call_to_number):
        return f"“Идет звонок на номер {call_to_number}” с сим-карты-{sim_card_number} - Beeline"

class Smarthone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list, ):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)





    def use_gps(self, location):
        return f"через 100 метров круто поверните на право, в соторону {location}"

    
comp =Computer(7, 512)
tel =Phone(2)
smart_1 = Smarthone(4, 128, 4)
smart_2 = Smarthone(8, 512, 6)