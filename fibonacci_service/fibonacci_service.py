import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(filename='logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def get_fibonacci():

    number = int(request.args.get('number'))

    if number is None:
      number = 1

    fibonacci = fibo(number)

    return { 'fibonacci': fibonacci }


def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')