from app.data.data import Cache

res = Cache.find('user',[('id','=',1210)])
print(res)
# Cache.cache_dumps()
# 测试数据
input('press any key to exit')