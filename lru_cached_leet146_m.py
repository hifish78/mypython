class LRUCache:
    """
       dictionary + double linked list
       so we can make put & get operation in O(1) time

       The dictionary can keep track of the keys and its values in the double linked list. That results in O(1) time for
       put and get operation and allows to remove the first added node in O(1) time as well.

       One advantage of double linked list is that the node can remove itself without other reference.
       In addition, it takes constant time to add and remove nodes from the head or tail.

       近期最多使用的放于头部，最少使用的放在尾部。 那么每次缓存达到上限的时候，删除尾部即可，其余为链表的基础操作模拟即可。

       要点：
       1) 数据结构： dictionary + double linked list,  cache {} => key: value (value存的是NODE)
       2) 基本需要一个全局变量SIZE维护DOUBLE LINKED LIST的元素个数，这个值需要和capacity比较，如果超过，需要从尾部删除元素。
       3) 只要做了个GET或者PUT操作，就意味这访问过这个NODE了，这个NODE都必须要挪到头部
       4） 挪到头部 = 删除这个NODE + 加到头部
       5）当新加一个NODE的时候，需要和CAPACITY比较，如果超过了，需要从尾部删除这个元素，也必须要从dictionary里面删除这个元素

       3) get :
          a) 如果NODE不存在，return -1
          B) 存在的话， 找到这个NODE, 把这个NODE 挪到头部 （挪到头部意味这先从原来位置删除这个NODE, 然后ADD到头部）
        3）PUT:
           a) 如果找到KEY, 也就是说NODE存在，更新VALUE, 挪到头部
           B) 如果没有找到KEY， 也就是说NODE不存在，那么应该新建一个NODE, 然后加到头部。 当新加一个NODE到头部的时候，需要检查是不是超过了
           capacity，如果超过了，需要从尾部删除一个元素。
    """

    def __init__(self, capacity):


    def get(self, key):

    def put(self, key, value):
