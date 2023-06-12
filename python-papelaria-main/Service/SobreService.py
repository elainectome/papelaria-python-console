from Repositorio.SobreRepositorio import SobreRepositorio

class SobreService:
    def __init__(self):
        self.repositorio = SobreRepositorio()

    def getAll(self):
        return self.repositorio.getAll()
    
    def getById(self, idSobre):
        return self.repositorio.getById(idSobre)
    