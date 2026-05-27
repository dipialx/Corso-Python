import redis
from redis_search import *

r = redis.Redis(host="localhost", port=6379, decode_responses=False)

INDEX_NAME = "idx:sherlock"

print(r.keys("sherlock:chunk:*")[:5])
print(len(r.keys("sherlock:chunk:*")))
print(r.ft(INDEX_NAME).info())

results = redis_search("Sherlock")

