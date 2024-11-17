class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors
    def __len__(self):
         return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def _eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

hightower = House('Гринландия', 12)
warehouse = House('Подвал', 12)

print(hightower)
print(warehouse)
print(hightower == warehouse)
print(warehouse.__add__(13))
print(hightower == warehouse)
print(hightower < warehouse)
print(hightower <= warehouse)
print(hightower > warehouse)
print(hightower >= warehouse)
print(hightower != warehouse)
print(hightower.__radd__(4))
print(warehouse.__iadd__('5'))
print(warehouse.__iadd__(11))