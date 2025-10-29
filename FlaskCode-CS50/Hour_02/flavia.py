class Person:
    def __init__(self):
        self.bladder_full = False  # Initialize bladder state
    
    def check_bathroom_status(self, bladder_full):
        if self.bladder_full == True:
            return "Alert: Time for a toilet break!"  # Fixed indentation
        else:
            return "You can hold it for now... maybe grab a coffee"
        
fred = Person()
fred.check_bathroom_status(True)