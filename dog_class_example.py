#Dog example
class dog:
    
    #Define the attributes by calling the __init__ function
    def __init__(self,name,age):
        #We can use the input variables as attributes
        self.name = name
        self.age = age
        #We can also create default attributes
        self.awake = True
        
        
    #Create the method that controls the sleep pattern of the dog
    def order(self,order):
        if order == 'sleep':
            if self.awake:
                print('Guau (OK, I will sleep, I am tired)')
                #We can modify attributes inside the instances
                self.awake = False
            else:
                pass #The dog is already sleeping, cannot talk
        if order == 'awake':
            if self.awake:
                print('Guau guau guau (I am awake, and hungry, feed me!)')
            else:
                print('Guaaaau (Good morning!)')
                #We can modify attributes inside the instances
                self.awake = True 