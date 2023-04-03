
import os

class DBRouter:

    dbname = os.environ.get('ENV_MODE')
    if(dbname is None): dbname = 'local'

    def db_for_read(self, model, **hints):
        return self.dbname

    def db_for_write(self, model, **hints):
        return self.dbname

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.dbname
