class super_klas:
    def __init__(self, init_val):
        self.num_val = init_val
        
    def print_val(self):
        print ("hex val = " + hex(self.num_val))
        

myKlas = super_klas(1234567)
myKlas.print_val()

wtf = 0
print ((" Hello World " + str(wtf)) * 2)