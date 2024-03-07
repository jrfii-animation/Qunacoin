from mongoengine import Document, StringField, IntField, FloatField, EmbeddedDocument, EmbeddedDocumentListField, ListField

class Transaction(EmbeddedDocument):
    sender = StringField(required=True)
    recipient = StringField(required=True)
    amount = FloatField(required=True)
    fee = FloatField(required=True)
    signature = StringField(required=True)

class Block(Document):
    height = IntField(required=True)
    prev_hash = StringField(required=True)
    merkle_root = StringField(required=True) 
    timestamp = IntField(required=True)
    nonce = StringField(required=True)
    transactions = ListField(EmbeddedDocumentField(Transaction))
    
    meta = {
        "indexes": ["height", "prev_hash"]
    }