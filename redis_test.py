import redis

r = redis.Redis(host='localhost', port=6379)


r.set("chiavechenonesiste", "valore della chiave che nonesiste")
print(r.get("chiavechenonesiste"))


print(r.get("nome"))

r.set("nome", "Python")

print(r.get("nome"))