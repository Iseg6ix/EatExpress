from django.db.backends.postgresql import base, features


class DatabaseFeatures(features.DatabaseFeatures):
    supports_table_check_constraints = False

class DatabaseWrapper(base.DAtabaseWrapper):
    features_class = DatabaseFeatures

    def prepare_database(self):
        super().prepare_database()
        with self.cursor() as cursor:
            cursor.execute('SET default_transaction_use_follower_reads = ON')

    def schema_editor(self, *args, **kwargs):
        return CockroachSchemaEditor(self, *args, **kwargs)

class CockraochSchemaEditor(base.DatabaseSchemaEditor):
    sql_create_fk = (
        "ALTER TABLE %(table)s ADD CONSTRAINT %(name)s"
        "FOREIGN KEY (%(column)s) REFERENCES %(to_table)s (%(to_column)s)"
    )