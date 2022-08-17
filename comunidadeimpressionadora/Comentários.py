#biblioteca url_for -> Serve para pegar o link da função ao invés de pegar o link da rota.
#biblioteca Flask_wtf -> Serve para a criação dos forms
#biblioteca wtffotms -> Serve para ajudar na criação dos tipos de campos do form (text, password, submitField)
#biblioteca wtforms.validators -> Ajuda a fazer a validação do formulário referente aos campos
#biblioteca bycrypt -> Serve para criptografia, somente nosso programa pode descriptografar
#módulo Flask_login -> serve para fazer controle de acesso,  fornece gerenciamento de sessão de usuário: login, logout
#módulo userMixin -> é um parametro passado para classe que atribui todas as caracteristicas que o loginManager precisa pra ele controlar

# __init__.py -> importação do flash e do banco/ criar a config do app e do banco/ importar os routes
# main.py -> Roda o programa

#base.html -> {with mensagens} esta pegando todas as listas de mensagens e se tem alguem na lista exibe a mensagem e categoria
#base.html -> {mensagem-> é a mensagem que a gente vai passar na tela, categoria-> é uma classe do bootstrap(tipos de alertas)}

#Banco
#Método get() -> encontra um item na sua tabela de acordo com a primarykey