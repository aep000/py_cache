class redis_cache:
    def __init__(self,config):
        self.r = config["redis"]

    def cache(self,key,func, timeout, *args, **kwargs):
        out = self.r.get(key)
        if out == None:
            print "did not cache"
            out = func(*args, **kwargs)
            self.r.set(key,out,ex=timeout)
        return out
