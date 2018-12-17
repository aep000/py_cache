from flask import Flask
from pycache import Cache, Flask_Cache
import redis

r = redis.Redis(host='localhost', port=6379)

x=1
y=2


app = Flask(__name__)
cache = Flask_Cache(app, mode="redis",config ={"redis":r})


@app.route("/")
@cache.cache_route()
def hello():
    print ("I AM NOT CACHED")
    return "Hello World!"


@cache.cache_on_args([0,1])
def add(x,y):
    print "Add is not cached"
    return x+y

print add(x,y)
