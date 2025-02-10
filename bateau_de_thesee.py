class Part():
    def __init__(self,name,material):
        self.name=name
        self.material=material

    def change_material(self,new_material):
        self.material=new_material
    
    def __str__(self):
        print(f"{self.name} est composée de {self.material}")
    
class Ship(Part):
    def __init__(self,name,material,parts):
        super().__init__(name,material)
        self.__parts={parts.name for part in parts}
    def display_state(self):
        for part in self.__parts.values():
            print(part)

    def replace_part(self,part_name,new_part):
        self.name=part_name
        self.__parts[part_name]=new_part
        return self.__parts
        


part1=Part("voile","papier")

part2=Part("ancre","metal")
ship1=Ship("voile","papier")


ship1.display_state()

ship1.replace_part(part1,part2)

ship1.display_state()