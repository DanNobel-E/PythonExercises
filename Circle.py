import CircleUtils
import math
import matplotlib.pyplot as plt

class Circle:
    
    def __init__(self, center, radius=0, diameter=0):
        self.center= center
        self.radius= abs(radius) if diameter ==0 else abs(diameter*0.5)
        self.circumference = 2*self.radius * math.pi
        self.area = self.radius**2 * math.pi
        
    def draw(self,color, x_lim= (-1,1), y_lim= (-1,1)):
        circle=plt.Circle(self.center,self.radius,color= color)
        fig, ax = plt.subplots() 
        ax.add_patch(circle)
        ax.set_xlim(x_lim[0],x_lim[1])
        ax.set_ylim(y_lim[0],y_lim[1])
        plt.show()
        
    def print(self):
        line1 =" Center: { " + f"x: {self.center[0]} y: {self.center[1]}" + "}" + f" | Radius: {self.radius}"
        line2 = f" Circumference: {self.circumference} | Area: {self.area}"
        header_length = len(line1) if len(line1) >= len(line2) else len(line2)
        header= "\n["
        footer= "["
        for n in range(header_length-1):
            header+= "-"
            footer+="-"
        header+="]"
        footer+="]\n"
        print(header)
        print(line1)
        print(line2)
        print(footer)
        
        
        
if __name__ == '__main__':
    circle0= Circle((-7,0),3.14)
    circle1= Circle((2,3),5)
    circle2= Circle((1,2),1)
    c= CircleUtils.CircleUtils(circle0,circle1,circle2)
    #c.sort("area")
    c.print()
    c.draw(['red','blue','white'], (-10,10), (-10,10))
    
    #c.print()
    # circle.print()
    # circle.draw('r', (-5,5), (-5,5))
    
