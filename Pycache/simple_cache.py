class simple_cache:
    def __init__(self,config):
        self.config=config
        self.cache = dict()
    def cache(self, key, func, timeout=-1, *args, **kwargs):
        if(key in self.cache):
            return self.cache[key]
        out = func(*args, **kwargs)
        self.cache[key]=out
        return out
