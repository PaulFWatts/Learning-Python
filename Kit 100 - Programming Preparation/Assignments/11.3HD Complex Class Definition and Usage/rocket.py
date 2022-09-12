
# Rocket class defination for Task 11.3HD

class Rocket:

   #####################
   # main constructor method for creating rockets 
   #####################
   def __init__(self, model, manufacturer,escapeVelocity):
        self.model = model;
        self.manufacturer = manufacturer
        self.speed = 0
        self.landed = True
        self.escapeVelocity = escapeVelocity

   #####################
   # Get the landing status of the rocket
   #####################
   def getIsLanded(self):
       return self.landed

   #####################
   # Get the current escape velocity in this universe..
   #####################
   def getEscapeVelocity(self):
       return self.escapeVelocity

   #####################
   # Try and take off.. 
   #####################
   def takeOff(self):
       if self.landed:
          self.landed = False
          print("Taking off, speed is currently",self.getSpeed())
       else:
          print("Error - cannot take off as already flying!")

   #####################
   # Try and land.. Can only land if speed is zero.
   #####################
   def land(self):    
       if not(self.landed):
          if self.getSpeed() > 0:
              print("Error - cannot land as speed is not zero!")
          else:
             print("Rocket landed!")
             self.landed = True
       else:
          print("Error - cannot land as already landed!")

   #####################
   # accelerate the rocket i.e. increase speed
   #####################
   def accelerate(self):
        if not(self.landed):
           self.speed += 5
        else:
           print("Error - cannot accelerate as landed!")
        
   #####################
   # decelerate the rocket i.e. decrease speed
   #####################
   def decelerate(self):
        if not(self.landed):
           if self.speed >= 5:
              self.speed -=5
           else:
              print("Error - cannot decelerate below zero, rocket would crash!")
        else:
           print("Error - cannot decelerate as landed!")

   #####################
   # Get the rocket's current speed
   #####################
   def getSpeed(self):
        return self.speed    

   #####################
   # Get the rocket's model
   #####################
   def getModel(self):
      return self.model

   #####################
   # Get the rocket's manufacturer
   #####################
   def getManufacturer(self):
      return self.manufacturer
