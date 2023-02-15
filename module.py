class Kategoria:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.tulelok:int = int(v[1])
        self.eltuntek:int = int(v[2])