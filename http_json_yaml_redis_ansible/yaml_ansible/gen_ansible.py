import yaml
import sys
import logging
import os
#from yaml.loader import SafeLoader

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

with open("./todo.yml", "r") as f:
    try:
        data = yaml.safe_load(f)
    except yaml.YAMLError:
        logging.error("YAML error load()")
        sys.exit(1)

dest = './prod/'

deploy = []
deployH =   [{ 
                'name': 'processing boom',
                'hosts': 'all',
                'become': 'yes',
                'tasks': deploy
            }]

packages = data.get('server').get('install_packages')
for i in packages:
    _dict = {
                'name': 'install ' + i,
                'apt':
                    {'name': i,}
            }
    deploy.append(_dict)

copy = data.get('server').get('exploit_files')
for i in copy:
    _dict = {
                'name': 'copy ' + i[:-3],
                'copy':
                    {'src': i, 'dest': dest}
            }
    deploy.append(_dict)

_dict = {
            'name': 'run script exploit',
            'ansible.builtin.script': dest + 'exploit.py',
            'args':
                {'executable': 'python3'}
        }
deploy.append(_dict)

bad_guys = ','.join(data.get('bad_guys'))
_dict = {
            'name': 'run script',
            'ansible.builtin.script': dest + 'consumer.py -e ' + bad_guys,
            'args':
                {'executable': 'python3'}
        }
deploy.append(_dict)

with open("./deploy.yml", "w") as f:
    try:
        f.write(yaml.dump(deployH, sort_keys=False))
    except yaml.YAMLError:
        logging.error("YAML error dump()")
        sys.exit(1)
logging.info("Create file deploy.yml")
