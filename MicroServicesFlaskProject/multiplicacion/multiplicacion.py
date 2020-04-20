from flask import Flask
from flask import request
import traceback
import json
from flask_cors import CORS, cross_origin
from waitress import serve

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

@app.route('/api/multiplicacion', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type'])
def multiplicacion(): 
    try:
        firstNumber = int(request.args.get('firstNumber'))
        secondNumber = int(request.args.get('secondNumber'))
        resultOp = firstNumber * secondNumber
        result = json.dumps(resultOp)
        return str(result)
    except ValueError:
        return "Debe ingresar dos números para poder calcular la multiplicacion"
    except Exception:
        return traceback.format_exc()

if __name__ == '__main__':
   serve(app, port='4730')