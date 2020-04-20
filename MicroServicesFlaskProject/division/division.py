from flask import Flask
from flask import request
import traceback
import json
from flask_cors import CORS, cross_origin
from waitress import serve

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

@app.route('/api/division', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type'])
def division(): 
    try:
        firstNumber = int(request.args.get('firstNumber'))
        secondNumber = int(request.args.get('secondNumber'))
        if secondNumber == 0:
            return 'No se puede hacer una division por 0'
        else:
            resultOp = firstNumber / secondNumber
            result = json.dumps(resultOp)
        return str(result)
    except ValueError:
        return "Debe ingresar dos números para poder calcular la division"
    except Exception:
        return traceback.format_exc()

if __name__ == '__main__':
   serve(app, port='4740')