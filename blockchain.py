import json
import datetime
import hashlib




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
        """ 
            is used to produce the cryptographic hash of each block based on the above values.

            Returns:
                [type]: imported the SHA-256 algorithm into the cryptocurrency blockchain project to help in getting the hashes of the blocks.
        """
        encoded_block = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def block_data(self):
        """
            resulted new block

            Returns:
                dict: [description]
        """
        return {
            "hash": self.code_hash(), 
            "index":self.index,
            "timestamp":self.timestamp, 
            "nonce":self.nonce,
            "previous_hash": self.previous_hash,
            "data": self.data,
            }



class BlockChain:


    __NOW_DATE = datetime.datetime.now()


    def __init__(self):
        """
            instantiates the blockchain

           - self.chain — this variable stores all the blocks.
           - self.current_data — this variable stores information about the transactions in the block.
           - self.build_genesis() — this method is used to create the initial block in the chain.
        """
        self.chain = []
        self.data_current = []
        self.genesis_block()


    def genesis_block(self):
        """
            method is used for creating the initial block in the chain
        """
        self.build_block(nonce=1, previous_hash='0')


    def build_block(self, nonce, previous_hash):
        """
        transactions

        Args:
           - nonce ([int]): randomly incremented so that the result of the hash function on the block satisfies
           - previous_hash ([int]): contains the result of the hash function on the previous block

        Returns:
            block
        """

        block = Block(
            index= len(self.chain) + 1,
            timestamp= str(self.__NOW_DATE),
            nonce= nonce,
            previous_hash= previous_hash,
            data= self.data_current
        )

        self.data_current = []

        self.chain.append(block.block_data())
        
        return block


    def get_last_block(self):
        """
            last block

        Returns:
            dict block
        """
        return self.chain[-1]


    def add_transaction(self, sender, receiver, amount, time):
        """ data of transactions on a block

        Args:
            sender ([type]): sender’s information
            receiver ([type]):  receiver’s information
            amount ([type]): amount send 
            time ([type]): time transactions
        """

        self.data_current.append({
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'time': str(self.__NOW_DATE)
})


    def hash(self, block):
        """
        generator previous_hash

        Args:
            block ([type]): [description]

        Returns:
            [type]: [description]
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def proof_of_work(self):
        """is by taking the latest block and add a nonce such to satisfy tha

        Returns:
            [type]: [description]
        """

        previous_block = self.get_last_block()

        previous_nonce = previous_block['nonce']

        previous_hash = self.hash(previous_block)

        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(
                str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        #return new_nonce
        return self.build_block(new_nonce, previous_hash)


    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True




# ----------------------------------- print--------------------------
blockchain = BlockChain()
node_address = "a0ea10d5b483109573c882de44"
root_node = '006cc49ce412b7c4ee5e48588e68e10'

def mine_block():
    blockchain.add_transaction(
    sender=root_node, 
    receiver=node_address, 
    amount=1.15, 
    time=str(datetime.datetime.now()))

    block = blockchain.proof_of_work()
    response = {
                'message': 'Success a block!',
                'index': block.block_data()['index'],
                'timestamp': block.block_data()['timestamp'],
                'nonce': block.block_data()['nonce'],
                'previous_hash': block.block_data()['previous_hash'],
                'transactions': block.block_data()['data'],
                }
    return response


for item in range(0,10):
    print(mine_block())