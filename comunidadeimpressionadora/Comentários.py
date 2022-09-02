#biblioteca url_for -> Serve para pegar o link da função ao invés de pegar o link da rota.
#biblioteca Flask_wtf -> Serve para a criação dos forms
#biblioteca wtffotms -> Serve para ajudar na criação dos tipos de campos do form (text, password, submitField, filefield)
#biblioteca wtforms.validators -> Ajuda a fazer a validação do formulário referente aos campos
#biblioteca bycrypt -> Serve para criptografia, somente nosso programa pode descriptografar
#módulo Flask_login -> serve para fazer controle de acesso,  fornece gerenciamento de sessão de usuário: login, logout
#módulo userMixin -> é um parametro passado para classe que atribui todas as caracteristicas que o loginManager precisa pra ele controlar

# __init__.py -> importação do flash e do banco/ criar a config do app e do banco/ importar os routes
# main.py -> Roda o programa

#navbar.html -> metodo url_for é uma variavel python, precisa usar {{}}. Redireciona para
#base.html -> {with mensagens} esta pegando todas as listas de mensagens e se tem alguem na lista exibe a mensagem e categoria
#base.html -> {mensagem-> é a mensagem que a gente vai passar na tela, categoria-> é uma classe do bootstrap(tipos de alertas)}
#editar_perfil.html -> l51, Reconhece o form porque foi passado no return na função editar_perfil
#perfil.html -> l28, tem a logica que ao clicar no bt editar perfil redireciona para a pagina editar perfil

#Banco
#Método get() -> encontra um item na sua tabela de acordo com a primarykey

######################################DICAS######################################
#{% for usuario in lista_usuarios %}        <!--usar "%" quando for algume estrutura, ex: if, for-->
#           {{ usuario }}                   <!--sem "%" quando for variavél-->
#*****passo a passo para criação de forms -> criar a rota do form/criar o html do form/criar a class do form/importar o form no routes/instanciar a classe/implementar o form no html. Aula35 do curso
#ctrl + r -> faz troca de texto
#sempre que vc criar um form que recebe arquivo dentro da tag form precisa receber o o parametro enctype, que é o tipo de criptografia e reconhece o tipo de arquivo
