class hash_table:
    def __init__(self):
        self.max=20
        self.arr=[None for i in range(self.max)]
    
    def get_key(self,key):
        h=0
        for char in key:
            h=h+ord(char)
        return h%self.max
    def __setitem__(self,key,val):
        g=self.get_key(key)
        self.arr[g]=val
    def __getitem__(self,key):
        h=self.get_key(key)
        print( self.arr[h])  
    def __delitem__(self,key):
        h=self.get_key(key)
        del(self.arr[h])
        

if __name__=='__main__':
    t=hash_table()
    t.get_key('march 6')
    t['march 6']=130
    t['march 1']=120
    t['march 17']=150
    t['march 6']
