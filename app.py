from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from typing import List

# Simulando um "banco de dados" em memória
usuarios = []

#! Definição dos tipos GraphQL
type_defs = """
    type Usuario {
        nome: String!
        idade: Int!
        cidade: String!
    }

    type Query {
        usuarios: [Usuario!]!
    }

    type Mutation {
        criarUsuario(nome: String!, idade: Int!, cidade: String!): Usuario!
        deletarUsuario(nome: String!): String!
    }
"""

#! Definição dos resolvers para Query
query = QueryType()

@query.field("usuarios")
def resolve_usuarios(_, info):
    return usuarios

#! Definição dos resolvers para Mutation
mutation = MutationType()

@mutation.field("criarUsuario")
def resolve_criar_usuario(_, info, nome: str, idade: int, cidade: str):
    usuario = {"nome": nome, "idade": idade, "cidade": cidade}
    usuarios.append(usuario)
    return usuario

@mutation.field("deletarUsuario")
def resolve_deletar_usuario(_, info, nome: str):
    global usuarios
    # Filtra os usuários, mantendo apenas os que não possuem o nome especificado
    usuarios = [usuario for usuario in usuarios if usuario["nome"] != nome]
    return f"Usuário {nome} deletado com sucesso!"

# !schema executável
schema = make_executable_schema(type_defs, query, mutation)

# Configuração o aplicativo ASGI
app = GraphQL(schema)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)