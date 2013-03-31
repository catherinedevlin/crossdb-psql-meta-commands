from collections import namedtuple
from sqlalchemy import inspect, create_engine, MetaData, Table
import re

class Connection(object):
    def __init__(self, conn):
        self.connect_string = conn
        self.engine = create_engine(self.connect_string)
        self.inspector = inspect(self.engine)
        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect()
    dt_tuple = namedtuple('dt_tuple', ['Schema', 'Name', 'Type', 'Owner'])
    def dt(self, pattern=None, S_include_system_objects=False, extra_info=False):
        for table in self.metadata.sorted_tables:
            if (not pattern) or (re.search(pattern, table.name)):
                result = self.dt_tuple(
                    Schema = table.schema or 'Public',
                    Name = table.name,
                    Type = str(type(table)),
                    Owner = '?'
                    )
                yield result
                    
conn = Connection('postgresql://will:longliveliz@localhost/shakes')
for tbl in conn.dt():
    print(tbl)
    
class Reporter(object):
    def parse(self, txt):
        if not txt.startswith(r'\\'):
            raise NotImplementedError('Command %s not recognized' % txt)
        commands = list(txt[1:])
        return commands
   
     