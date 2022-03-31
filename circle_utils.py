
import matplotlib.pyplot as plt


class CircleUtils:
    
    def __init__(self, *args):
        self.circles= []
        for circle in args:
            if(type(circle) is list):
                for c in circle:
                    self.circles.append(c)
            else:     
                self.circles.append(circle)
            
            
    def sort(self, sort_field, sort_reversed=False):
        self.circles= sorted(self.circles, key = lambda x: getattr(x,sort_field), reverse= sort_reversed)
        return self.circles
    
    def draw(self,colors, x_lim= (-1,1), y_lim= (-1,1)):
        circles_to_draw= []
        color= None
        for i,circle in enumerate(self.circles):
            if i < len(colors):
                color= colors[i]
            else:
                color= 'black'
            circles_to_draw.append(plt.Circle(circle.center,circle.radius,color= color))
        fig, ax = plt.subplots() 
        for circle in circles_to_draw:
            ax.add_patch(circle)
        ax.set_xlim(x_lim[0],x_lim[1])
        ax.set_ylim(y_lim[0],y_lim[1])
        plt.show()

    def print(self):
        for circle in self.circles:
            circle.print()
