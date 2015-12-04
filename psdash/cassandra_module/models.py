from datetime import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model


class Machine(Model):
    id = columns.Text(partition_key=True)
    updated_at = columns.DateTime(primary_key=True, default=datetime.now())

    # state attributes
    cpu_usage = columns.Float()
    disks = columns.List(columns.Float)
    memory_usage = columns.Float()


def sync_db():
    sync_table(Machine)


def connect():
    connection.setup(['localhost'], 'major')
