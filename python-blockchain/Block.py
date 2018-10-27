# Creating the Block class
import hashlib
import datetime


class Block:
    def __init__(self, index=0, timestamp=datetime.datetime.now().__str__(), data="Genesis Block", previous_hash=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def create_genesis_block(self):
        # Manually construct a block with
        # index zero and arbitrary previous hash
        genesis_block = Block(0, datetime.datetime.now().__str__(), "Genesis Block", "0")
        return genesis_block

    def next_block(self, last_block):
        this_index = last_block.index + 1
        this_data = "Block " + str(this_index)
        this_hash = last_block.hash
        next_block_chain = Block(this_index, datetime.datetime.now().__str__(), this_data, this_hash)
        return next_block_chain