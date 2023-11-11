from views.home import home
from models.usuario_model import adicionar_usuario, ler_usuarios

def home_controller():
    primeiro_usuario = ler_usuarios()[0]["nome"]
    return home(nome_de_usuario=primeiro_usuario)