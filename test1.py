from Pycache import Cache
import redis

r = redis.Redis(host='localhost', port=6379)
cache = Cache(mode="redis",config ={"redis":r})

x=1
y=2

@cache.cache_custom_key(str(x)+str(y))
def add(x,y):
    print "Add is not cached"
    return x+y

print add(x,y)
