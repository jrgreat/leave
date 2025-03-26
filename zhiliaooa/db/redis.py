import redis

r = redis.Redis(host="192.168.121.131", port=6379, db=0)

value = r.get('k1')

pass

if __name__=="__main__":
    pass