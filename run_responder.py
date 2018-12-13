import responder
import time

import models_responder2 as models

api = responder.API()

@api.route('/hello/{who}')
def say_hello(req, resp, *, who):
    params = req.params.get('id', '')
    resp.headers['X-Pizza'] = '42'
    resp.status_code = 200
    resp.media = {
      'Hello': who,
      'param': params
    }

@api.background.task
def sleep(s=10):
    time.sleep(s)
    print('slept!')

@api.add_route('/', static=True)
def index(req, resp):
    resp.content = api.template('index.html')

@api.route('db/signin')
def signin(req, resp):
    datas = req.media
    resp.media = {'successfully signed in':models.signin(datas)}

@api.route('/db/login')
def login(req, resp):
    datas = req.media()
    resp.media = {'isAccount':models.isAccount(datas)}

if __name__ == '__main__':
    api.run()
