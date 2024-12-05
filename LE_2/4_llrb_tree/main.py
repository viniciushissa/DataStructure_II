import random
from llrb import LLRBTree

tree = LLRBTree()
random_numbers = random.sample(range(1, 100001), 10000)

for number in random_numbers:
    tree.put(number)

print("Altura da árvore:", tree.height(tree.root))