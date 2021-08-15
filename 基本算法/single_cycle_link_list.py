class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self,node = None):
        self.__head = node
        node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem,end = " ")
            cur = cur.next
        print(cur.elem)
        print("")


    def add(self,item):
        node = Node(item)
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = self.__head


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur  = self.__head
            while cur.next != None:
                cur = cur.next
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
            pre  = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node





    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next

                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while cur.next != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False




if __name__ == '__main__':
    ll = SingleLinkList()
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
