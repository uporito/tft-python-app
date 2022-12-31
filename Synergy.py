class Synergy :
    
    def __init__(self, name : str, units : list[str], levels : list[int]) -> None:
        self.name = name
        self.units = units
        self.levels = levels

    def __str__(self) -> str:
        return f'{self.name} - units : {self.units}, levels : {self.levels}.'