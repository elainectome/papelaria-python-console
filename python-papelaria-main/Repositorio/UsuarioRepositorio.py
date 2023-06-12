from BancoDados.ConfiguracaoDB import get_db
from Entidade.Usuario import Usuario

class UsuarioRepositorio:
    def __init__(self):
        self.db = next(get_db())
    
    def getAll(self):
        return self.db.query(Usuario).all()

    def getById(self, id_usuario):
        return self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    
    def criarUsuario(self, usuario):
        self.db.add(usuario)
        self.db.commit()

    def updateUsuario(self, usuario):
        self.db.merge(usuario)
        self.db.commit()

    def deleteUsuario(self, id_usuario):
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario is not None:
            self.db.delete(usuario)
            self.db.commit()
