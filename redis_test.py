import redis

r = redis.Redis(host='localhost', port=6379)


print(r.get("nome"))

r.set("nome", "Python")

print(r.get("nome"))