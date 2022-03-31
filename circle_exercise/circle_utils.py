
import matplotlib.pyplot as plt

class CircleUtils:
    
    @staticmethod
    def __list_circles__(*args):
        args= args[0]
        circles= []
        for circle in args:
            if(type(circle) is list):
                for c in circle:
                    circles.append(c)
            else:     
                circles.append(circle)
        return circles
    
    @staticmethod      
    def sort(*args, sort_field, sort_reversed=False):
        circles= CircleUtils.__list_circles__(args)
        circles= sorted(circles, key = lambda x: getattr(x,sort_field), reverse= sort_reversed)
        return circles
    
    @staticmethod
    def draw(*args, colors, x_lim= (-1,1), y_lim= (-1,1)):
        circles= CircleUtils.__list_circles__(args)
        circles_to_draw= []
        color= None
        for i,circle in enumerate(circles):
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
        
    @staticmethod
    def print(*args):
        circles= CircleUtils.__list_circles__(args)
        for circle in circles:
            circle.print()
