class mechanism:
    def __init__(self,config):
        self.config = config

    def cache(self,key,func, timeout, *args, **kwargs):
        return func(*args, **kwargs)

class redis_cache(mechanism):
    def __init__(self,config):
        self.r = config["redis"]
        mechanism.__init__(self,config)

    def cache(self,key,func, timeout, *args, **kwargs):
        out = self.r.get(key)
        if out == None:
            out = func(*args, **kwargs)
            self.r.set(key,out,ex=timeout)
        return out

class simple_cache(mechanism):
    def __init__(self,config):
        mechanism.__init__(self,config)
        self.cache = dict()
    def cache(self, key, func, timeout=-1, *args, **kwargs):
        if(key in self.cache):
            return self.cache[key]
        out = func(*args, **kwargs)
        self.cache[key]=out
        return out
