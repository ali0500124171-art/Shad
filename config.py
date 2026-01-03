
from main import r, MockRedis

token = '8223507502:AAE8Vi0C0vxkgDHX5WzQ8dx6rMOikZnwOqc'
Dev_Zaid = token.split(':')[0]
sudo_id = 8087077168
botUsername = 'A7718BOT'
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')