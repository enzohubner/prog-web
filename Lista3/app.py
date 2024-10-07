from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confimacao = request.form['confirmaSenha']
        
        if senha != confimacao:
            return 'As senhas não conferem!', 400
        
        idade = request.form['idade']
        
        return redirect(f'/resposta/{nome}/{email}/{senha}')
    else:
        return render_template('formulario.html')

@app.route('/resposta', methods=['GET'])
def resposta():
    return render_template('resposta.html')
    

if __name__ == '__main__':
    app.run(debug=True)
