from node import Node

class LLRBTree:
    def __init__(self):
        self.root = None

    def is_red(self, node): # Vermelho -> True / Preto -> False
        if not node:
            return False
        return node.color 

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = True
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = True
        return x

    def flip_colors(self, h):
        h.color = True
        h.left.color = False
        h.right.color = False

    def insert(self, h, key):
        if not h:
            return Node(key, True)

        if key < h.key:
            h.left = self.insert(h.left, key)
        elif key > h.key:
            h.right = self.insert(h.right, key)
        else:
            pass

        if self.is_red(h.right) and not self.is_red(h.left): # h (preto)           x (preto)
            h = self.rotate_left(h)                          #  \             ->  /
                                                             #   x (vermelho)    h (vermelho)

        if self.is_red(h.left) and self.is_red(h.left.left): #        h (preto)             x (preto)
            h = self.rotate_right(h)                         #       /                     / \
                                                             #      x (vermelho)  -> y (vermelho) h (preto)
                                                             #     /
                                                             #    y (vermelho) Xnão podeX

        if self.is_red(h.left) and self.is_red(h.right): #            h (preto)                 h (vermelho)
            self.flip_colors(h)                          #           / \             ->        / \
                                                         # x (vermelho) y (vermelho)    x (preto) y (preto)

        return h

    def put(self, key):
        self.root = self.insert(self.root, key)
        self.root.color = False

    def height(self, node=None):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))