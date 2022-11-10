import heapq

# Node of a Huffman Tree
# initial setup

# getting user input from the user - might move later, but it works for now
# test different types of strings here

# let user enter a string
user_input = input("User input (string): ")
print(user_input)


# nested class


class Nodes:


    def __init__(self, frequency, symbol, left=None, right=None):

        # the frequency of the occurance
        self.frequency = frequency

        # the symbol
        self.symbol = symbol

        # the left node - of the current node
        self.left = left

        # the right node - of the current node
        self.right = right

        # the tree direction - will be 0 or 1 - will address this later on - empty string
        self.direction = ''

        # DELETE - idk yet

        # def childern(self):
        #     return self.left, self.right

        # def __dir__(self):
        #     return self.left, self.right


# def CalculateProbability(the_data):


# frequency of characters?

# we can take a string and then figure this out


def Frequency (input):

    symbols_in_input = dict()

    for symbols in input:
        if symbols_in_input.get(symbols) == None:
            symbols_in_input[symbols] = 1
        else:
            symbols_in_input[symbols] += 1

        # else:
        #    print()

        # sorting
        #.sort(reverse = True)

    return symbols_in_input

# def HuffmanTree (input):

    # base case: empty string
    # if len (text) == 0:
    # return




def Output (user_input, evaluation):

    # leave empty
    output = []
    #storage = []

    for type in user_input:

        # append
        output.append(evaluation[type])

    # String join - String join() Method
    the_string = ''.join([str(item) for item in output])
    return the_string



eval = dict()



def Find(node, data=''):

    # a huffman code for current node
    newValue = data + str(node.direction)

    if (node.left):

        #left
        Find(node.left, newValue)

    if (node.right):

        #right
        Find(node.right, newValue)

        # nor left or right
    if (not node.left and not node.right):
        eval[node.symbol] = newValue

    return eval

# compression - will be done later if time allows


#def Output (user_input, evaluation):

    # leave empty
 #   output = []
    #storage = []

  #  for type in user_input:

        # append
   #     output.append(evaluation[type])

    # String join - String join() Method
    #the_string = ''.join([str(item) for item in output])
    #return the_string



def Compression (user_input, evaluation):


    # total bit space to store the data before compression

    postCompression = 0

    # 8 bit
    preCompression = len(user_input) * 8

    symbols = evaluation.keys()

    for occurances in symbols:

        the_count = user_input.count(occurances)
        # calculating how many bit is required for that symbol in total
        postCompression += the_count * len(evaluation[occurances])



    # print statements
    print("pre compress efficiency ", preCompression)
    print("post compress efficiency ", postCompression)



def encodedOutput(input):


    symbols = Frequency(input)
    present_symbols = symbols.keys()
    frequency = symbols.values()

    # print statements
    print("individual symbols (only once): ", present_symbols)
    print("frequency: ", frequency)

    the_nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in present_symbols:
        the_nodes.append(Nodes(symbols.get(symbol), symbol))

    while len(the_nodes) > 1:


        # sorting all the nodes in ascending order based on their frequency
        # sort all the nodes in ascending order
        # based on their frequency
        # left = heapq.heappop(nodes)
        # right = heapq.heappop(nodes)

        the_nodes = sorted(the_nodes, key=lambda x: x.frequency)


        # picking two smallest nodes
        right = the_nodes[0]
        left = the_nodes[1]

        # values for the direction on the tree - assignment of directional values
        left.direction = 0
        right.direction = 1

        # So now we can combine the 2 smallest nodes to create (one) new node that will be the parent
        createNode = Nodes(left.frequency + right.frequency, left.symbol + right.symbol, left, right)

        # keep in mind to give single letter groups precedence over multiple letter groups


        the_nodes.remove(left)
        the_nodes.remove(right)

        # the_nodes.remove()

        the_nodes.append(createNode)

    huffmanEncoding = Find(the_nodes[0])
    print("Symbols with codes" , huffmanEncoding)

    Compression(input, huffmanEncoding)
    encodedOutput = Output(input, huffmanEncoding)
    print("Encoded output" , encodedOutput)





    return encodedOutput, the_nodes[0]

    # print("symbols: ", present_symbols)
    # print("frequency of letter occurance: ", frequency)


def Decoding (data, huffmanTree):

    treeHead = huffmanTree
    # encodedOutput()
    output = []

    for x in data:

        # right
        if x == '1':
            huffmanTree = huffmanTree.right

        # left
        elif x == '0':
            huffmanTree = huffmanTree.left

        try:
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:
                pass
            print("left - none | right - none")

        except AttributeError:

            # .append symbol
            output.append(huffmanTree.symbol)
            huffmanTree = treeHead


    string = ''.join([str(item) for item in output])
    return string


# the_data = "Sally sells seashells by the seashore"
# print(the_data)


encoding, the_tree = encodedOutput(user_input)



#def Compression (user_input, evaluation):
    # total bit space to store the data before compression

    # 8 bit
 #   preCompression = len(user_input) * 8
  #  postCompression = 0
   # the_symbols = evaluation.keys()

    #for occurance in the_symbols:
#
 #       the_count = user_input.count(occurance)
  #      postCompression += the_count * len(evaluation[occurance])

   # print("pre compression:", preCompression)
    #print("post compression:", postCompression)


# **  Print Statements for both Encoded and Decoded **
print("Encoded output", encoding)
print("Decoded Output: ", Decoding(encoding, the_tree))

# TEST STRINGS

# Sally sells seashells by the seashore.
# Peter Piper picked a peck of pickled peppers a peck of pickled peppers Peter Piper
# picked.
# Houston, the Eagle has landed.
# Is that your final answer?

# Print statements
