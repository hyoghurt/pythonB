import redis
import time
import json
import sys
import logging

#funct switch
def process_switch(data, bad_guys):
    logging.debug('Get message %s', data)
    _metadata = data['metadata']
    _from = _metadata['from']
    _to = _metadata['to']
    _amount = data['amount']
    if _to in bad_guys:
        if _amount > 0:
            _metadata.update( {"from": _to, "to": _from} )
    print (data)

#start program
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

if len(sys.argv) != 3:
    logging.error("Wrong number of arguments. [Need 2 : comsumer.py -e 111111111,2222222222]")
    sys.exit(1)

if sys.argv[1] != "-e":
    logging.error("Wrong first argument. [-e]")
    sys.exit(1)

#check second arg is 10 digit
try:
    bad_guys = list(map(int, sys.argv[2].split(',')))
    for i in bad_guys:
        if i < 999999999 or i > 9999999999:
            raise ValueError
except ValueError:
    logging.error("Wrong second argument. Argument should consist of exactly 10 digits")
    sys.exit(1)
logging.debug(bad_guys)

#connect redis
r = redis.Redis(charset='utf-8', decode_responses=True)
p = r.pubsub()
p.subscribe("broker")

logging.info("Starting program consumer")
while True:
    message = p.get_message()

    if message:
        if message['type'] == 'message':
            process_switch(json.loads(message['data']), bad_guys)
            #print (str(message['data'], 'utf-8'))
    time.sleep(0.001)
