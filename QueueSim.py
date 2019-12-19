import salabim as sim




# -----------------------------------------------------------
# 3 classes are used 
# -- Customer generator class
# -- Clerk class
# -- Customer class
# -----------------------------------------------------------
 
class CustomerGenerator(sim.Component):  # customer generator class
    def process(self):
        while True:
            Customer()
            yield self.hold(sim.Uniform(5,15).sample()) # sampling process

# takes a random number out of this uniform distribution with lower point 5 and upper point 15
# and waits for that certain time interval before generating the next customer             
            
            
class Customer(sim.Component): # customer class
    def process(self):
        self.enter(waitingline)
        if clerk.ispassive():
            clerk.activate()
        yield self.passivate()

# After the customer has been generated it enters the queue and checks if the Clerk is idle and activates it 
# and waits for that certain time interval before generating the next customer              
        
        
        
class Clerk(sim.Component): # Clerk class
    def process(self):
        while True:
            while len(waitingline) == 0:
                yield self.passivate()
            self.customer = waitingline.pop()
            yield self.hold(30)
            self.customer.activate()

# If the clerk is active it takes the first customer inline 
# and holds it for the specified time (30)            
            

env = sim.Environment(trace = True)

CustomerGenerator()
clerk = Clerk()
waitingline = sim.Queue("waitingline")

env.run(till = 50)
print()
waitingline.print_statistics()