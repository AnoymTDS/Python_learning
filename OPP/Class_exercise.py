
import random

def accout_num_gene():
  x = random.randrange(100000,10000000)
  return x

class People:
    
 def __init__(self, p_fname, p_age):
    self.p_fname = p_fname
    self.p_age = p_age
        
 def __str__(self):
    return self.p_fname
 

 class Bank:
    
    def __init__(self, bank_name,):
        self.bank_name, = bank_name
       
        
    