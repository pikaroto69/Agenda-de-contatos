from flask import Flask, render_template, request, redirect
app = Flask(__name__)  #instancia o flask

#lista
contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)
@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        codigo = len(contatos)
        contatos.append([codigo, nome, telefone, email])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        contatos[codigo] = [codigo, nome, telefone, email]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  # Renderiza o formulário de edição
@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial



if __name__ == '__main__':
    app.run(debug=True) #executa o aplicativo flask
