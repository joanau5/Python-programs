#lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python


# Joana Ugarte
# joanau@uci.edu
# 44875730

import random

"""
The default numbers here are generally good enough to create a rich tree. 
You are free to play with the numbers if you want. Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

TREE_DEPTH = 5
NODE_DEPTH = 5

def tree_builder(nodes:list, level:int, acorn:str) -> list:
    """
    Builds a tree using the random integers selected from the tree_depth and node_depth defaults
    """
    r = random.randrange(1, NODE_DEPTH)
    for i in range(r):
        if level < TREE_DEPTH:
            level_id  = f"L{level}-{i}"
            if level_id == acorn:
                level_id += "(acorn)"
            n = [level_id]
            nodes.append(tree_builder(n, level+1, acorn_placer()))

    return nodes

def acorn_placer() -> str:
    """
    Returns a random acorn location based on tree_depth and node_depth defaults
    """
    return f"L{random.randrange(1,TREE_DEPTH)}-{random.randrange(1,NODE_DEPTH)}"

def recursive_acorn(nlist):
    acorns = 0
    new = []
    for i in nlist:
        if type(i) == list:
            recursive_acorn(i)
        else:
            if 'acorn' in i:
                acorns+=1
                print(i)
                print(acorns)
                new.append(i)


def run():
    # create a tree and start placing acorns
    tree = tree_builder([], 1, acorn_placer())
    recursive_acorn(tree)
    
    # end solution

if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")

    run()
