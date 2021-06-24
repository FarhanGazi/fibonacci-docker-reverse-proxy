import random
import logging

from flask import Flask

app = Flask(__name__)
logging.basicConfig(filename='logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def get_number():
    num = random.randint(1, 10)
    return { 'number': num }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')