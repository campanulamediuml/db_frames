调用from app.data.data import Cache进行缓存处理（缓存处理下，第一次启动需要加载整个数据库，时间比较久）


调用from app.data.server import Data进行对数据库的直接操作

单次读取数据小于2万条不建议使用缓存

接口：
res = select('table',[('col','=','xx')])
res == [{key1:value1,key2:value2,...},{key1:value1,key2:value2,...}]


res = find('table',[('col','=','xx')])
res == {key1:value1,key2:value2,...}


res = insert('table',{key1:value1,key2:value2,...})

res = delete('table',[('col','=','xx')])

res = update('table',[('col','=','xx')],{key1:value1,key2:value2,...})



