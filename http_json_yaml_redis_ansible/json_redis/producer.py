#wget http://download.redis.io/redis-stable.tar.gz
#tar xvzf redis-stable.tar.gz
#cd redis-stable
#make
#./src/redis-server

#pip install redis
import redis
import json
import logging

#return json
def mes(_from, _to, _amount):
    date = {
       "metadata": {
           "from": _from,
           "to": _to
       },
       "amount": _amount
    }
    logging.info("Message = %s", date)
    return json.dumps(date)

#logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

#start program
r = redis.Redis()
logging.info("Started")

r.publish("broker", mes(1111111111, 2222222222, 10000))
r.publish("broker", mes(3333333333, 4444444444, -3000))
r.publish("broker", mes(2222222222, 5555555555, 5000))

logging.info("Finished")
