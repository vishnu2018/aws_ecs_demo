'''
cicd demo
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    '''
    cicd demo
    '''
    return 'Hello world! CI/CD demo successful'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
