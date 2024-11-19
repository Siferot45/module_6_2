from Sedan import Sedan


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
print('\n')

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('BLACK')
vehicle1.set_color('Green')
vehicle1.set_color('Purple')
vehicle1.set_color('Pink')
vehicle1.set_color('Brown')
vehicle1.set_color('Orange')
vehicle1.owner = 'Vasyok'
print('\n')

# Проверяем что поменялось
vehicle1.print_info()
