from collections import Counter
import queue

text = open('rand_file').read() # read from the file

# count the symbols probability
count_ = Counter(text)
sum = count_['A'] + count_['B'] + count_['C'] + count_['D'] + count_['E']
a_probability = count_['A'] / sum
b_probability = count_['B'] / sum
c_probability = count_['C'] / sum
d_probability = count_['D'] / sum
e_probability = count_['E'] / sum
# all_ = (a_probability+b_probability+c_probability+d_probability)
# print (all_, a_probability, b_probability, c_probability, d_probability, sum, count_)


class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.left, self.right))

freq = [(a_probability, 'A'), (b_probability, 'B'), (c_probability, 'C'), (d_probability, 'D'),(e_probability, 'E') ]

def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue
    return p.get()               # 3. tree is complete - return root node

node = create_tree(freq)
print(node)

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],HuffmanNode):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)

code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.10f}'.format(i[0]), code[i[1]])


str_enc = ""
for decoded in text:
    if decoded == 'A':
        str_enc = str_enc + code['A']
    elif decoded == 'B':
        str_enc = str_enc + code['B']
    elif decoded == 'C':
        str_enc = str_enc + code['C']
    elif decoded == 'D':
        str_enc = str_enc + code['D']
    else:
        str_enc = str_enc + code['E']

print (str_enc)


# with open("encoded_file","w") as f:
#      f.write(str_enc)
