from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres or comprimento <= 0:
        return "ERRO: Parâmetros inválidos."
    
    senha_lista = []
    
    if incluir_maiusculas:
        senha_lista.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        senha_lista.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        senha_lista.append(random.choice(string.digits))
    if incluir_simbolos:
        senha_lista.append(random.choice(string.punctuation))

        caracteres_restantes = comprimento - len(senha_lista)
    
    if caracteres_restantes > 0:
        for _ in range(caracteres_restantes):
            senha_lista.append(random.choice(caracteres))

        random.shuffle(senha_lista)
    
    return "".join(senha_lista)[:comprimento]

@app.route('/', methods=['GET', 'POST'])
def index():
    senha_gerada = None
    
    if request.method == 'POST':
        try:
            
            comprimento = int(request.form.get('comprimento', 12))
            
            
            maiusculas = request.form.get('maiusculas') == 'on'
            minusculas = request.form.get('minusculas') == 'on'
            numeros = request.form.get('numeros') == 'on'
            simbolos = request.form.get('simbolos') == 'on'

           
            if comprimento < 4:
                comprimento = 4 

            
            senha_gerada = gerar_senha(
                comprimento=comprimento,
                incluir_maiusculas=maiusculas,
                incluir_minusculas=minusculas,
                incluir_numeros=numeros,
                incluir_simbolos=simbolos
            )
            
        except ValueError:
            senha_gerada = "ERRO: O comprimento deve ser um número inteiro."
            
    
    return render_template('index.html', senha=senha_gerada)

if __name__ == '__main__':
    app.run(debug=True)