import threading
import random
import time

 
class Philosopher(threading.Thread):
 
    running = True
 
    def __init__(self, xname, forkLeft, forkRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkLeft = forkLeft
        self.forkRight = forkRight
 
    def run(self):
        while(self.running):
            time.sleep( random.uniform(3,10))
            print ('%s is hungry.' % self.name)
            self.dine()
 
    def dine(self):
        fork1, fork2 = self.forkLeft, self.forkRight
 
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            #if locked:
            if locked: break
                #while(fork2.acquire(False)):
                    #time.sleep( random.uniform(3,10))
                    #print ('%s waiting for second fork.' % self.name)
                    #self.dining()
            fork1.release()
        else:
            return
 
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):			
        print ('%s starts eating dinner'% self.name)
        time.sleep(random.uniform(1,10))
        print ('%s finishes eating and start thinking.' % self.name)
 
def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('P1','P2','P3','P4', 'P5')
 
    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]
 
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print ("Now all philosofer are finishing.")
 
DiningPhilosophers()
