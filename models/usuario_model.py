usuarios = [
    {
        "nome": "Teste1",
        "idade": 10
    },
    {
        "nome": "Teste2",
        "idade": 20
    },
    {
        "nome": "Teste3",
        "idade": 30
    }
]

def adicionar_usuario(nome, idade):
    usuarios.append({
        "nome": nome,
        "idade": idade
    })

def ler_usuarios():
    return usuarios