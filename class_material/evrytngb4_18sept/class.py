class Atom:
    def __init__(self,elec, protons, MW, name):
        self.elec = elec
        self.protons = protons
        self.MW = MW
        self.name = name

hydrogen = Atom(1,1,1,"hydrogen")
print(hydrogen.elec)