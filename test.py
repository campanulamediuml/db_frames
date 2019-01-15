from app.data.data import Cache
from app.data.server import Data
import time

time_1 = time.time()
res = Cache.select('sb_log',[('user_id','=',1210)])
print(len(res))
print('第一次读取缓存大表用时:',time_1-time.time())
for i in res:
    print(i)

time_1 = time.time()
res = Cache.select('sb_log',[('user_id','=',1210)])
print(len(res))
print('第二次读取缓存大表用时:',time_1-time.time())
for i in res:
    print(i)

time_1 = time.time()
res = Data.select('sb_log',[('user_id','=',1210)])
print(len(res))
print('直接读取大表用时:',time_1-time.time())
for i in res:
    print(i)

# Cache.cache_dumps()

input('press any key to exit')