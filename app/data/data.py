from app.data.base_method.dbserver.cache import cached_base
    
class Cache(object):
    base = cached_base()

    @staticmethod
    def get_tables():
        return Cache.base.get_tables()

    @staticmethod
    def cache_dumps():
        return Cache.base.cache_dumps()

    @staticmethod
    def find(table,conditions,fields = '*'):
        return Cache.base.find(table,conditions,fields)

    @staticmethod
    def select(table, conditions, fields='*'):
        return Cache.base.select(table, conditions, fields)