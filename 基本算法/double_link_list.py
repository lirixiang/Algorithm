class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.prev = None
        self.next = None

class DoubleLinkList(object):
    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):

        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem,end = " ")
            cur = cur.next
        print("")


    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self. __head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            #cur.next = node
            node.__head = node
            cur.next = self.__head



    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node

        else:
            cur  = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = self.__head
            cur.next = node

    def insert(self,pos,item):
        """
        指定位置添加元素
        :param pos 从零开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:

            node = Node(item)
            cur  = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next =cur
            node.prev = cur.prev
            node.prev.next = node
            cur.prev = node





    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    pass
                else:
                   pre.next = cur.next

                break
            else:

                cur = cur.next

    def search(self,item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False




if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.travel()
    ll.insert(2,100)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
    ll.remove(9)
    ll.travel()
