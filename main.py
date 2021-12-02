import hashlib
from Block import Block
blockchain = []

main_block = Block("T Rex Waffle",["Alec sent 1 BTC to Eric",
"Eric sent 5 BTC to Sam"
"Alec sent 1 BTC to Sam"]) 
#These would usually not be strings but transaction products
#genesis = first block
#mining is how you come up with blocks

second_block = Block(main_block.block_hash, ["Scooter sent 2 BTC to Eric", "Gary sent 3 BTC to Alec"])

third_block = Block(second_block.block_hash, ["A to C 5 BTC", "F to B 10 BTC"])

print("Block hash: Genesis Block")
print(main_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)

print("Block hash: Third Block")
print(third_block.block_hash)