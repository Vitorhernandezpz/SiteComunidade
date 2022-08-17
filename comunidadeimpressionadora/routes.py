from flask import render_template, request, flash, redirect, url_for
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.models import Usuario

lista_usuarios = ['vitor', 'ernande',' joao', 'maria']


@app.route("/")#decorator
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/lista-usuario')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET','POST'])
def login():
    form_login = FormLogin()                                                                      # Instancia dos formularios
    form_criar_conta = FormCriarConta()                                                           # Instancia dos formularios
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))                                                                 # redireciona p  url da função home
    if form_criar_conta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta) #Passa pro html as informações
