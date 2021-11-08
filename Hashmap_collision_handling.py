import csv
class hash_table:
    def __init__(self):
        self.max=20
        self.arr=[[] for i in range(self.max)]
    
    def get_key(self,key):
        h=0
        for char in key:
            h=h+ord(char)
        return h%self.max
    def __setitem__(self,key,val):
        g=self.get_key(key)
        found = False
        for indx,ele in enumerate(self.arr[g]):
            if ele[0]==key  and len(ele)==2:
                ele[0][indx]=(key,val)
                found=True
        if not found:
            self.arr[g].append((key,val))
    def __getitem__(self,key):
        h=self.get_key(key)
        for indx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                print(ele[1])  
    def __delitem__(self,key):
        h=self.get_key(key)
        for indx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                del(self.arr[h][indx])
        

if __name__=='__main__':
    t=hash_table()
    data=open("Temp_humidity.csv")
    csv_reader=csv.reader(data)
    data_line=list(csv_reader)
    data_line=data_line[1:]
    for i in data_line:
        k=i[0]
        t[k]=i[1]
    print(t.arr)