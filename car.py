class Car (object):
     def __init__ (self, model, company, color):
        self.model = model
        self.company = company
        self.color = color
     def start (self):
         print ("started")
     def stop (self):
         print ("stopped")

#creating object for the class Car
bmw = Car ("wheel", "window", "seat")
print( bmw.start() )
print( bmw.stop()  )