class Cache:
    available_modes={
    "basic": 1,
    "redis": 2,

    }
    def __init__(mode="basic",config={}):
        self.mode = self.available_modes[mode]
        self.config = config
        if(self.mode == 1):
            self.cache = simple_cache(config)
        elif(self.mode == 2):
            self.cache = redis_cache(config)

    def __keygen_generic(func, *args, **kwargs):
        out = ""
        for arg in args:
            out+=str(args)
        for key, arg in kwargs:
            out += str(key) + str(name)
        return func.__name__()+out


    def cacheSimple(timeout=-1):
        #TODO add none redis cache timeout
        def wrapperContainer(func):
            def function_wrapper(*args, **kwargs):
                self.cache.cache(__keygen_generic(func, *args, **kwargs),func)
            return function_wrapper
        return wrapperContainer

    def cache_custom_key(key):
        #TODO add none redis cache timeout
        def wrapperContainer(func):
            def function_wrapper(*args, **kwargs):
                self.cache.cache(key,func)
            return function_wrapper
        return wrapperContainer
