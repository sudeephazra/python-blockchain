import Block
import json
import datetime


def test_blockchain_python():
    block = Block.Block()
    # Create the blockchain and add the genesis block
    blockchain = [block.create_genesis_block()]
    previous_block = blockchain[0]
    num_of_blocks_to_add = 5

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = block.next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

    # Prints the entire blockchain in JSON form
    for i in range(0, blockchain.__len__()):
        print(json.dumps(blockchain[i].__dict__))

    print("########################################")
    # Printing the original block
    print(json.dumps(blockchain[2].__dict__))
    # Tampering with the block data
    blockchain[2].data = "Modified"
    # Re-hashing the block
    blockchain[2].hash = Block.Block.hash_block(blockchain[2])
    # Printing the tampered block
    print(json.dumps(blockchain[2].__dict__))
    print("########################################")

test_blockchain_python()