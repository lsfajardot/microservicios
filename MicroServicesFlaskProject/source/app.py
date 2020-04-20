from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from waitress import serve
import json
import requests
import traceback

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route("/")
def main():
    # return "Hello Flask!"
    return render_template('app.html')


# Funciones Calculadora
@app.route('/send', methods=['GET', 'POST'])
def send(sum=sum):
    if request.method == 'POST':
        firstNumber = request.form['firstNumber']
        secondNumber = request.form['secondNumber']
        operation = request.form['operation']

        if operation == 'add':
            sum = (requests.get('http://suma:4710/api/suma?firstNumber='+firstNumber+'&secondNumber='+secondNumber)).text
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = (requests.get('http://resta:4720/api/resta?firstNumber='+firstNumber+'&secondNumber='+secondNumber)).text
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = (requests.get('http://multiplicacion:4730/api/multiplicacion?firstNumber='+firstNumber+'&secondNumber='+secondNumber)).text
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = (requests.get('http://division:4740/api/division?firstNumber='+firstNumber+'&secondNumber='+secondNumber)).text
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html,', sum="Debe ingresar los numeros para calcular")




# Llamado de los servicios - test.
# @app.route('/sumar')
# def sumar():
#     firstNumber = "88"
#     secondNumber = "22"
#     opSuma = requests.get('http://suma:4710/api/suma?firstNumber='+firstNumber+'&secondNumber='+secondNumber)
#     return opSuma.text

# @app.route('/restar')
# def restar():
#     firstNumber = "50"
#     secondNumber = "20"
#     opResta = requests.get('http://resta:4720/api/resta?firstNumber='+firstNumber+'&secondNumber='+secondNumber)
#     return opResta.text

# @app.route('/multiplicar')
# def multiplicar():
#     firstNumber = "6"
#     secondNumber = "8"
#     opMultiplicacion = requests.get('http://multiplicacion:4730/api/multiplicacion?firstNumber='+firstNumber+'&secondNumber='+secondNumber)
#     return opMultiplicacion.text

# @app.route('/dividir')
# def dividir():
#     firstNumber = "150"
#     secondNumber = "15"
#     opDivision = requests.get('http://division:4740/api/division?firstNumber='+firstNumber+'&secondNumber='+secondNumber)
#     return opDivision.text



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port='4700')
