import os

fs_stat = os.statvfs('/')
block_size = fs_stat[0]
total_blocks = fs_stat[2]
free_blocks = fs_stat[3]

total_space = block_size * total_blocks
free_space = block_size * free_blocks

print("Total filesystem size:", total_space, "bytes")
print("Free filesystem space:", free_space, "bytes")