from equipos.models import ExternalModel

class EquipoRouter(object):
    def db_for_read(self, model, **hints):
        if issubclass(model, ExternalModel):
            return 'support'

        return 'default'

    def db_for_write(self, model, **hints):
        if issubclass(model, ExternalModel):
            return None

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return (isinstance(obj1, ExternalModel) == isinstance(obj2, ExternalModel))

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'support':
            return False
        return (db == 'default')
