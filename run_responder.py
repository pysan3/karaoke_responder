import responder
import time

import models_responder as models

api = responder.API()

@api.route("/hello/{who}")
def say_hello(req, resp, *, who):
    params = req.params.get("id", "")
    resp.headers["X-Pizza"] = "42"
    resp.status_code = 200
    resp.media = {
      "Hello": who,
      "param": params
    }

@api.background.task
def sleep(s=10):
    time.sleep(s)
    print("slept!")

@api.route("/")
def hello(req, resp):
    sleep()
    resp.content = "processing"

@api.route("/db/login")
async def login(req, resp):
    datas = await req.media()
    resp.media = {"isAccount":models.isAccount(datas)}

if __name__ == '__main__':
    api.run()
