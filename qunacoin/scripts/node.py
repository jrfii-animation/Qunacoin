import qunacoin
from qunacoin.core.p2p import QunaCoinNode

def main(node_config):
  
    # Initialize node state
    node = QunaCoinNode(node_config)
    
    # Start P2P server
    node.run()
    
    # Begin mining process
    qunacoin.mining.mine(num_cycles=1000)
    
if __name__ == "__main__":
    node_config = { 
        "host": "0.0.0.0",
        "port": 8545, 
        "seeds": [
            ("seed1.qunacoin.org", 8545),
            ("seed2.qunacoin.org", 8545),
            # ...
        ]
    }
    main(node_config)