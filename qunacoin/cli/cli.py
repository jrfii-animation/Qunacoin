import click
from qunacoin.core import ledger, crypto
from qunacoin.db import db

@click.group()
def cli():
    pass

@cli.command()
def create_wallet():
    """Create a new QunaCoin wallet"""
    qcrypto = crypto.get_qcrypto()
    public_key, private_key = qcrypto.generate_keypair()
    click.echo(f"Public Key: {public_key}")
    click.echo(f"Private Key: {private_key}")

@cli.command()
@click.argument("wallet_addr")    
def get_balance(wallet_addr):
    """Get the balance of a wallet address"""
    balance = ledger.get_balance(wallet_addr)
    click.echo(f"Balance: {balance} QunaCoin")
    
@cli.command()
@click.argument("sender_wallet")
@click.argument("recipient_addr") 
@click.argument("amount", type=float)
def send_coins(sender_wallet, recipient_addr, amount):
    """Send QunaCoin from one wallet to another"""
    ledger.send_coins(sender_wallet, recipient_addr, amount)
    
# ... other CLI commands    

if __name__ == "__main__":
    cli()