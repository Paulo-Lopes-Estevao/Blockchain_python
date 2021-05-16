import json
import datetime




class Block:


    def __init__(self,**kwargs):
        """
           - index — it’s used to track the position of a block within the blockchain
           - previous_hash — it used to reference the hash of the previous block within the blockchain.
           - data — it gives details of the transactions done, for example, the amount bought.
           - timestamp— it inserts a timestamp for all the transactions performed.
        """
        self.index = kwargs['index']
        self.data = kwargs['data']
        self.nonce = kwargs['nonce']
        self.previous_hash = kwargs['previous_hash']
        self.timestamp = kwargs['timestamp']


    def code_hash(self):
        pass


    def block_data(self):
        pass



class BlockChain:


    def __init__(self):
        pass


    def genesis_block(self):
        pass


    def build_block(self):
        pass


    def get_last_block(self):
        pass


    def add_transaction(self, sender, receiver, amount, time):
        pass


    def hash(self, block):
        pass


    def proof_of_work(self):
        pass


    def is_chain_valid(self, chain):
        pass


def mine_block():
    pass