import sys

class AWS:
    # class or static variable
    FILLER_VALUE = -int(sys.maxsize)
    
    def __init__(self, values):
        self.values = values[:] 

    def setValues(self, values):
        self.values = values[:]
        
    def getValues(self):
        # return self.values[:]        
        return self.values[:]

    def __str__(self):
        return "AWS [values=" + str(self.values) + "]"

    def remove(self,i):
        value = self.FILLER_VALUE
        if(i >= 0 and i < len(self.values) ):
            value = self.values[i]
            for index in range(i, len(self.values)-1):
                self.values[index] = self.values[index+1]
            self.values[len(self.values)-1] = self.FILLER_VALUE
        return value
    
    def fillAndExpand(self, position, nt):
        numberOfTimes = abs(nt)
        
        newArray = [0]*( len(self.values) + numberOfTimes )
        
# 		int[] newArray = new int[values.length + numberOfTimes];
             
        # Before the position  
        for i in range(0,position+1):
            newArray[i] = self.values[i]
                  

        # In the position
        for i in range(position, numberOfTimes + position+1):
            newArray[i] = newArray[position]
		

		# Make examples, so it is easier to visualize your methods
		#   p 1 2
		# a b c
		# a b b b c
		
        # After the position
        x = numberOfTimes

        for i in range(position+1, len(self.values)):
            newArray[i+x] = self.values[i]

        self.values = newArray[:]