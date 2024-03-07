import qunacoin.core.crypto as crypto

def encrypt_msg(msg, key):
    """Encrypt message with quantum key"""
    qcrypto = crypto.get_qcrypto()
    return qcrypto.encrypt(msg, key)

def decrypt_msg(msg, key):
    """Decrypt an encrypted message with the quantum key"""
    qcrypto = crypto.get_qcrypto()
    return qcrypto.decrypt(msg, key)

def send_msg(msg, peer):
    """Send encrypted message to peer"""
    peer.send(msg)

# ...