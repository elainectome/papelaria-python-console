from Repositorio.UsuarioRepositorio import UsuarioRepositorio
from Entidade.Usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repositorio = UsuarioRepositorio()

    def getAll(self):
        return self.repositorio.getAll()
    
    def getById(self, idUsuario):
        return self.repositorio.getById(idUsuario)
    
    def criarUsuario(self, nome, email, senha):
        usuario = Usuario(nome=nome, email=email, senha=senha)
        self.repositorio.criarUsuario(usuario)

    def updateUsuario(self, id_usuario, nome, email, senha):
        usuario = self.repositorio.getById(id_usuario)
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        self.repositorio.updateUsuario(usuario)

    def deleteUsuario(self, id_usuario):
        self.repositorio.deleteUsuario(id_usuario)
