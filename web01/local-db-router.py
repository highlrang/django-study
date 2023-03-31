
class LocalDBRouter:

    def db_for_read(self, model, **hints):
        return 'local'

    def db_for_write(self, model, **hints):
        return 'local'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'local'

