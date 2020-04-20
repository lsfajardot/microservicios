from flask import Flask
from flask import request
import traceback
import json
from flask_cors import CORS, cross_origin
from waitress import serve

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

@app.route('/api/suma', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type'])
def suma(): 
    try:        
        firstNumber = int(request.args.get('firstNumber'))  
        secondNumber = int(request.args.get('secondNumber'))
        resultOp = firstNumber + secondNumber
        result = json.dumps(resultOp)
        return result
    except ValueError:
        return "Debe ingresar dos números para poder calcular la suma"
    except Exception:
        return traceback.format_exc()

if __name__ == '__main__':
   serve(app,host='0.0.0.0', port='4710')