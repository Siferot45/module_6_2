class Vehicle:
    
    __COLOR_VARIANTS = ['brown', 'blue', 'red', 'green', 'yellow ', 'black', 'orange','purple ', 'white']
    
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner 
        self.__model = model 
        self.__color = color  
        self.__engine_power = engine_power 

    def get_model(self):
        return f"Модел: {self.__model}"
    
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    
    def get_color(self):
        return f"Цвет: {self.__color}"
    
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")
        
    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                return
                
        print(f"Нельзя сменить цвет на {new_color}")