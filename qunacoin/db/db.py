import mongoengine
from qunacoin.db import models

DB = None

def init_db(db_name, **kwargs):
    global DB
    DB = mongoengine.connect(db_name, **kwargs)
    
def get_db():
    if DB is None:
        raise Exception("No database connected")
    return DB

def drop_db():
    get_db().drop_database()
    
def add_block(block_data):
    Block = get_db().models.Block
    block = Block(**block_data)
    block.save()
    return block

def get_latest_block():
    Block = get_db().models.Block
    return Block.objects().order_by("-height").first()

def get_transaction(txid):
    # ...

# Other DB utility methods...