from setuptools import setup, find_packages

setup(
    name='TomAndKevinDataStructures',
    version='0.2',
    description='Data Structures',
    author='Tom',
    author_email='tom.stephen@icloud.com',
    packages=find_packages()
    # packages=['mylib, mylib.datastructures,\
    #         mylib.datastructures.trees,\
    #             mylib.datastructures.trees.AVL, mylib.datastructures.trees.BST, \
    #         mylib.datastructures.linear,\
    #             mylib.datastructures.linear.CDLL, mylib.datastructures.linear.CSLL\
    #             mylib.datastructures.linear.DLL, mylib.datastructures.linear.SLL, \
    #             mylib.datastructures.linear.Stack, mylib.datastructures.linear.Queue,\
    #         mylib.datastructures.nodes,\
    #             mylib.datastructures.nodes.Tree_Node, \
    #             mylib.datastructures.nodes.Doubly_linked_Node, mylib.datastructures.nodes.Single_linked_Node, \
    #         mylib.datastructures.heap, \
    #           mylib.datastructures.heap.VBH_Max, mylib.datastructures.heap.VBH_Min']
)