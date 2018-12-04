from redis_cache import redis_cache
class Cache:
    available_modes={
    "basic": 1,
    "redis": 2,

    }
    def __init__(self,mode="basic",config={}):
        self.mode = self.available_modes[mode]
        self.config = config
        if(self.mode == 1):
            self.cache = simple_cache(config)
        elif(self.mode == 2):
            self.cache = redis_cache(config)

    def __keygen_generic(self,func, *args, **kwargs):
        out = ""
        for arg in args:
            out+=str(args)
        for key, arg in kwargs:
            out += str(key) + str(name)
        return func.__name__()+out

    #probably shouldnt do this but it works for some things well
    def cache_simple(self,timeout=None):
        #TODO add none redis cache timeout
        def wrapperContainer(func):
            def function_wrapper(*args, **kwargs):
                return self.cache.cache(__keygen_generic(func, *args, **kwargs),func,timeout,*args, **kwargs)
            return function_wrapper
        return wrapperContainer

    def cache_custom_key(self,key,timeout=None):
        #TODO add none redis cache timeout
        def wrapperContainer(func):
            def function_wrapper(*args, **kwargs):
                return self.cache.cache(key,func,timeout, *args, **kwargs)
            return function_wrapper
        return wrapperContainer
