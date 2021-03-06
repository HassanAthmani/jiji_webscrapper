import flask
from flask_cors import CORS, cross_origin
import logging
from flask import request
import webscrapper


app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
@cross_origin(origin='*')
def scrapper():
    #header=request.headers.get('Authorization')
    #header =request.headers['Authorization']

    msg_received = flask.request.get_json()

    try:
        product=msg_received["product"]
        return webscrapper.jiji(msg_received)

    except (KeyError,TypeError):
        return {"Error": "No product provided to the scrapper", "statusCode": 404}



@app.route('/check', methods=['GET', 'POST'])
@cross_origin(origin='*')
def check():
    return "all is well"

@app.route('/scrap', methods=['GET', 'POST'])
@cross_origin(origin='*')
def with_param():

    product= str(request.args.get('product'))
    duration= str(request.args.get('duration'))
    fil= str(request.args.get('filter'))
    amount= str(request.args.get('amount'))
    #print(product+" "+duration+" "+fil+" "+amount)

    return webscrapper.jiji({"product":product,"filter":fil,"amount":amount,"time":duration})

def logga(info):
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.critical(info)




if __name__ == '__main__':
#pip install pyopenssl
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)

if __name__ != '__main__':

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


