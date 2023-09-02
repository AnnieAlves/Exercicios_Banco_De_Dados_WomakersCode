import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

"""
 1. Crie uma tabela chamada "alunos" com os seguintes campos:
id (inteiro), nome (texto), idade (inteiro) e curso (texto).
"""

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50));')


""" 
 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
"""

# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Anna",20,"Engenharia")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Luís",22,"Enfermagem")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Paulo",18,"Engenharia")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Roberta",18,"ADS")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Flávia",19,"Engenharia")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Luna",24,"ADS")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Fernando",21,"ADS")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Diana",22,"Advocacia")')
# # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(9,"Aline",19,"Engenharia")')


"""
3. Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
"""

""" a) Selecionar todos os registros da tabela "alunos". """

todos_alunos = cursor.execute('SELECT * from alunos')

print("\n\nTABELA DOS ALUNOS\n")
for aluno in todos_alunos:
    print(aluno)

""" b) Selecionar o nome e a idade dos alunos com mais de 20 anos. """

nome_idade_maiores_20 = cursor.execute('SELECT nome, idade from alunos WHERE idade >= 20')

print("\n\nAlunos com mais de 20 anos(inclusivo):\n")
for aluno in nome_idade_maiores_20:
    print(aluno)

""" c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética. """

alunos_engenharia_alfabetica = cursor.execute('SELECT * from alunos where curso = "Engenharia" ORDER BY nome')

print("\n\nAlunos de Engenharia em ordem Alfabética\n")
for aluno in alunos_engenharia_alfabetica:
    print(aluno)

""" d) Contar o número total de alunos na tabela."""

contador = cursor.execute('SELECT * from alunos')
total_alunos = 0
for _ in contador:
    total_alunos += 1
print(f'\n\nTotal de alunos: {total_alunos}\n')

"""
4. Atualização e Remoção:
"""

""" a) Atualize a idade de um aluno específico na tabela. """

# cursor.execute('UPDATE alunos SET idade = 23 WHERE nome="Luna"')




""" b) Remova um aluno pelo seu ID. """

# cursor.execute('DELETE from alunos WHERE id=7')




"""
 5. Criar uma Tabela e Inserir Dados:
Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
Insira alguns registros de clientes na tabela.
"""

# cursor.execute('CREATE TABLE clientes (id PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1,"Anna",20,8500)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2,"Fred",30,18900)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3,"Allan",50,12200)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4,"Giovanni",22,200)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5,"Lydia",25,850)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6,"Mariana",35,150)')





"""
6. Consultas e Funções Agregadas:
"""

""" a) Selecione o nome e a idade dos clientes com idade superior a 30 anos. """

clientes_mais_de_30 = cursor.execute('SELECT nome,idade FROM clientes WHERE idade >= 30')
print("\n\nCLientes com idade superior a 30 anos:\n")
for cli in clientes_mais_de_30:
    print(cli)




""" b) Calcule o saldo médio dos clientes. """

saldo_medio = cursor.execute('SELECT AVG(saldo) FROM clientes').fetchone()[0]
print(f"\n\n O saldo médio é de {saldo_medio}\n")




"""  c) Encontre o cliente com o saldo máximo. """

cliente_maior_saldo = cursor.execute('SELECT nome, MAX(saldo) FROM clientes').fetchone()
print(f"\n\nO cliente com maior saldo é: {cliente_maior_saldo}\n")




"""  d) Conte quantos clientes têm saldo acima de 1000 """

saldo_maior_1000 = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000').fetchone()[0]
print(f"\n\nQuantidade de cliente com saldo maior que R$1000,00: {saldo_maior_1000}\n")





"""  7. Atualização e Remoção com Condições """

""" a) Atualize o saldo de um cliente específico. """

#cursor.execute('UPDATE clientes SET saldo=5000.0 WHERE id=5')




""" b) Remova um cliente pelo seu ID """

# cursor.execute('DELETE from clientes WHERE id=6')



""" 
8. Junção de Tabelas 
 Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), 
 cliente_id (chave estrangeira referenciando o id da tabela "clientes"), 
 produto (texto) e valor (real). 
 Insira algumas compras associadas a clientes existentes na tabela "clientes".
 Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
"""

#  cursor.execute('''CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL,
#  FOREIGN KEY (cliente_id) REFERENCES clientes(id))''')

# cursor.execute(' INSERT INTO compras (id, cliente_id, produto, valor) VALUES(1,2, "Celular", 2000)')
# cursor.execute(' INSERT INTO compras (id,cliente_id,produto,valor) VALUES(2,2,"Televisão",3000)')
# cursor.execute(' INSERT INTO compras (id,cliente_id,produto,valor) VALUES(3,5,"Notebook",1000)')
# cursor.execute(' INSERT INTO compras (id,cliente_id,produto,valor) VALUES(4,1,"Tênis",100)')

consulta = '''
    SELECT clientes.nome, compras.produto, compras.valor
    FROM compras
    JOIN clientes ON compras.cliente_id = clientes.id
'''


dados_consulta = cursor.execute(consulta)


for resultado in dados_consulta:
    nome_cliente, produto, valor = resultado
    print(f'Cliente: {nome_cliente}, Produto: {produto}, Valor: R${valor:.2f}')


conexao.commit()
conexao.close()
