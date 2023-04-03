class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(list1,list2):
    list=[]
    list1=ListNode(list1)
    list2=ListNode(list2)
    while True:
        if list1.val==None:
                return list2
        elif list2.val==None:
                return list1
        elif list1.val>list2.val:
            list.append(list2.val)
            list2.next
        elif list1.val<list2.val:
             list.append(list1.val)
             list1.next
        else:
            list.append(list1.val)
            list.append(list2.val)
            list1.next
            list2.next






list1 = [1,2,4]
list2 = [1, 3, 4]
print(main(list1,list2))