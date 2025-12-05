## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

from empresa.config.database import SupabaseConnection
from empresa.dao.funcionario_dao import FuncionarioDAO
from empresa.dao.departamento_dao import DepartamentoDAO 

client = SupabaseConnection().client

# Criando DAO para acessar a tabela funcionario
funcionario_dao = FuncionarioDAO(client)

for funcionario in funcionario_dao.read_all():
    print(funcionario)

# Criando DAO para acessar a tabela departamento
departamento_dao = DepartamentoDAO(client)

for departamento in departamento_dao.read_all():
    print(departamento)