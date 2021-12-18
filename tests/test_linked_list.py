from linked_list import __version__, linked_list
from linked_list.linked_list import LinkedList, Node
import pytest

def test_node_instance():
    node = Node(1,None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_failure():
    node = Node(1,None)
    assert node.next != node
    assert node.value != 2

def test_Linked_List():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_empty_linked_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_to_linked_list():
    ll = LinkedList()
    # head is empty or none
    node1 = Node('apple')
    # ll.head is none
    ll.head == node1
    # ll.head is apple
    node2 = Node('pear')
    #apple.next is none
    node1.next = node2
    # apple.next is pear
    # apple goes to pear which goes to none
    ll.insert('banana')
    # new order is banana to apple to pear
    assert ll.head.value == 'banana'

def test_includes_in_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.includes('apple') == True

def test_includes_not_in_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.includes('yellow') != True

def test_version():
    assert __version__ == '0.1.0'
