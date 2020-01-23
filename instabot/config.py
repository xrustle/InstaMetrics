import json

with open('config.json', encoding='utf-8') as json_data_file:
    conf = json.load(json_data_file)

USER = conf['credentials']['username']
PASSWORD = conf['credentials']['password']
TOKEN = conf['token']
PROXY = conf['proxy']
ID = conf['id']
MONGO = conf['mongo']
API = conf['api']
MTPROTO = conf['mtproto']
