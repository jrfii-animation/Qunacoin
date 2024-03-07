import qunacoin.core.ledger.block as block
import qunacoin.core.ledger.transaction as transaction
import qunacoin.db.db as qunacoin_db

class BlockChain:

    def __init__(self):
        self.ledger = []
        # ...

    def validate_blockchain(self):
        """Validate entire blockchain"""
        # ...

    def add_block(self, new_block):
        """
        Add a new block of transactions to the blockchain.
        """

        # Validate block
        if not new_block.validate():
            return False

        # Check PoC work
        if not self.validate_proof_of_computation(new_block):
            return False

        # Choose opaque block representation
        compacted_block = # ...

        # Verify photonic quantum state from network consensus
        qstate = self.qstate_consensus(compacted_block)
        if not self.verify_qstate(qstate):
            return False

        # Update ledger
        self.ledger.append(new_block)

        # Write to DB
        qunacoin_db.add_block(new_block)

        return True

    def validate_proof_of_computation(self, block):
        """Validate the PoC work in a block"""
        # ...

    def qstate_consensus(self, block):
        """
        Quantum photonic consensus protocol.
        Returns the global qstate for the block to be verified.
        """
        # ...

    def verify_qstate(self, qstate):
        """Validate the global consensus qstate"""
        # ...

    # ...