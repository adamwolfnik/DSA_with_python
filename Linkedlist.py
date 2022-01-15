class Node:
  def __init__(self, data=None,next=None):
    self.data=data
    self.next=next

class Linked_list:
  def __init__(self):
    self.head=None

  def insert_at_beginining(self,data):
    node=Node(data, self.head)
    self.head=node

  def insert_at_end(self,data):
    if self.head is None:
      self.head=Node(data,None)
      return
    itr=self.head
    while itr.next:
      itr=itr.next
    itr.next =Node(data,None)

  def print(self):
    if self.head is None:
      print('Linked_lis is empty')
      return
    itr=self.head
    listr=''
    while itr:
      listr+= str(itr.data)+'-->'
      itr=itr.next
    print(listr)

  def insert_list(self,data_list):
    self.head=None
    for data in data_list:
      self.insert_at_end(data)

  def count_elements(self):
    itr=self.head
    count=0
    while itr:
      count+=1
      itr=itr.next

    return(count)

  def remove_elements(self,index):
    if index<0 or index>=self.count_elements():
      raise Exception("Invalid Index")
    if index==0:
      self.head=self.head.next
      return
    count=0
    itr=self.head
    while itr:
      if count==index-1:
        itr.next=itr.next.next
        break
      itr=itr.next
      count+=1

  def insert_elements(self,data,index):
    if index<0 or index>=self.count_elements():
      raise Exception("Invalid Index")
    if index==0:
      self.insert_at_beginining(data)
      return
    count=0
    itr=self.head
    while itr:
      if count==index-1:
        node=Node(data,itr.next)
        itr.next=node
        pass      
      count+=1
      itr=itr.next
  
  def insert_after_value(self,data_after,data_insert):
    itr=self.head
    while itr:
      if itr.data==data_after:
        node=Node(data_insert,itr.next)
        itr.next=node
      itr=itr.next
  
  def remove_by_value(self,data_remove):
    itr=self.head
    while itr:
      if itr.next.data==data_remove:
        itr.next=itr.next.next
        break
      itr=itr.next


if __name__=='__main__':
  l1=Linked_list()
  l1.insert_at_beginining(5)
  l1.insert_at_beginining(7)
  l1.insert_at_end(8)
  l1.print()
  l1.insert_list(['apple','orange','mango'])
  n=l1.count_elements()
  print(n)
  l1.remove_elements(1)
  l1.insert_elements('Jackfruit',1)
  l1.insert_after_value('Jackfruit','grapes')
  l1.print()
  l1.remove_by_value('grapes')
  l1.print()