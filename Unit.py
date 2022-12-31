class Unit :
    
    def __init__(self, name : str, cost : int, synergy_names : list[str]) -> None:
        self.name = name
        self.cost = cost
        self.synergy_names = synergy_names
        # TODO : stats = {'AD' : 50, 'AP' : 50}

    def __str__(self) -> str:
        return f'{self.name} - cost : {self.cost}, synergies : {self.synergy_names}.'