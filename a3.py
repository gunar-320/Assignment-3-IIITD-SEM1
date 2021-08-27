#GUNAR SINDHWANI 2020199 SECTION-B GROUP - 4

import numpy as np

import matplotlib.pyplot as plt
# NO other imports are allowed
#CLASS SHAPE NOT TO BE TOUCHED
#***********************************************************************************************************************************************
class Shape:

    def __init__(self):

        self.T_s = None

        self.T_r = None

        self.T_t = None

    def translate(self, dx, dy):

        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):

        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):

        rad = deg*(np.pi/180)

        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

    def plot(self, x_dim, y_dim):

        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim

        plt.plot((-x_dim, x_dim),[0,0],'k-')

        plt.plot([0,0],(-y_dim, y_dim),'k-')

        plt.xlim(-x_dim,x_dim)

        plt.ylim(-y_dim,y_dim)

        plt.grid()

        plt.show()
#***********************************************************************************************************************************************

class Polygon(Shape):

    def __init__(self, A):

        self.A=A

        self.ini_polygon=self.A[:] #to prevent aliasing or uncesseary changes due to changes in A in further steps

        self.A=np.array(self.A)

        self.ini_polygon=np.array(self.ini_polygon)

    def translate(self, dx, dy):
    
        x_coordinates = np.array([])
    
        y_coordinates = np.array([])
    
        self.ini_polygon=self.A[:] #to prevent aliasing or uncesseary changes due to changes in A in further steps
    
        self.A=np.transpose(self.A)
    
        Shape.translate(self,dx,dy)
    
        self.A=np.dot(self.T_t,self.A)
    
        for i in range(len(self.A[0])): #Rounding Off
        
            x_coordinates=np.append(x_coordinates,round(self.A[0][i],2))
    
            y_coordinates=np.append(y_coordinates,round(self.A[1][i],2))
    
        self.A=np.transpose(self.A)
    
        return (x_coordinates,y_coordinates)

    def scale(self, sx, sy):
    
        self.ini_polygon=self.A[:] #to prevent aliasing or uncesseary changes due to changes in A in further steps
    
        self.A=np.transpose(self.A)
    
        self.ini_centre_x=np.array([])
    
        self.ini_centre_y=np.array([])
    
        mem_count=0
    
        while True:
    
            self.ini_centre_x=np.append(self.ini_centre_x,self.A[0][mem_count])
    
            self.ini_centre_y=np.append(self.ini_centre_y,self.A[1][mem_count])
    
            mem_count+=1
    
            if mem_count == len(self.A[0]):
    
                break
    
        self.centre_x=np.sum(self.ini_centre_x , dtype=float) #finding sum of x - coordinates
    
        self.centre_y=np.sum(self.ini_centre_y , dtype=float) # finding sum of y - coordinates
    
        self.centre_x=(self.centre_x)/(len(self.ini_centre_x)) #finding x - coordinate of centre
    
        self.centre_y=(self.centre_y)/len(self.ini_centre_y) #finding y - coordinate of centre
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        Shape.translate(self,-self.centre_x,-self.centre_y) #STEP -1 Translate to Origin , by shifting the origin to Centre of Polygon
    
        z=np.transpose(self.A)
    
        self.A=np.dot(self.T_t,z)
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        Shape.scale(self,sx,sy) #STEP -2 SCALE
    
        n=np.transpose(self.A)
    
        self.A=np.dot(self.T_s,n)
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        self.A=np.transpose(self.A)
    
        Shape.translate(self,self.centre_x,self.centre_y) #step -3 TRANSLATING BACK TO INITIAL SYSTEM
    
        m=np.transpose(self.A)
    
        self.A=np.dot(self.T_t,m)
    
        x=np.around(self.A[0],decimals = 2) #ROUNDING OFF
    
        y=np.around(self.A[1] , decimals = 2) #ROUNDING OFF
    
        self.A=np.transpose(self.A)
    
        return (x,y)


    def rotate(self, deg, rx = 0, ry = 0):

        self.ini_polygon=self.A[:] #to prevent aliasing or uncesseary changes due to changes in A in further steps

        Shape.translate(self,-rx,-ry) #STEP -1 TRANSLATE to Origin!

        k=np.transpose(self.A)

        self.A = np.dot(self.T_t,k)

        self.A=np.transpose(self.A)

        self.A=np.transpose(self.A)

        self.A=np.transpose(self.A)

        Shape.rotate(self,deg) #STEP -2  ROTATE

        j=np.transpose(self.A)

        self.A=np.dot(self.T_r,j)

        self.A=np.transpose(self.A)

        self.A=np.transpose(self.A)

        self.A=np.transpose(self.A)

        Shape.translate(self,rx,ry) #STEP -3 Translate back to initial system of coordinates

        q=np.transpose(self.A)

        self.A=np.dot(self.T_t,q)

        x_coordinates=np.array([])

        y_coordinates=np.array([])

        for i in range(len(self.A[0])):

            x_coordinates=np.append(x_coordinates,np.round(self.A[0][i],2))

            y_coordinates=np.append(y_coordinates,np.round(self.A[1][i],2))

        final=(x_coordinates,y_coordinates)

        self.A=np.transpose(self.A)

        return final

    def plot(self):

        self.ini_polygon=np.transpose(self.ini_polygon) #one step behind polygon

        self.A=np.transpose(self.A)

        final_x = self.A[0] #x coordinates of final figure

        initial_x=self.ini_polygon[0] #x coordinates of final - 1 step figure

        final_y=self.A[1]

        initial_y = self.ini_polygon[1]

        self.ini_polygon=np.transpose(self.ini_polygon)

        self.A=np.transpose(self.A)

        plot_x=np.append(initial_x,final_x)  #process to find x-dim & y - dim , by finding highest of X and Y values!

        plot_y=np.append(initial_y,final_y)

        abs_plot_x=np.absolute(plot_x)

        max_plot_x=np.amax(abs_plot_x)

        abs_plot_y=np.absolute(plot_y)

        max_plot_y=np.amax(abs_plot_y)

        initial_x=np.append(initial_x,initial_x[0])

        initial_y=np.append(initial_y,initial_y[0])

        final_x=np.append(final_x,final_x[0])

        final_y=np.append(final_y,final_y[0])

        plt.plot(initial_x,initial_y,label = 'First' , linestyle = 'dashed')

        plt.plot(final_x,final_y,label = 'Second' , linestyle = 'solid')

        Shape.plot(self,max_plot_x,max_plot_y)

class Circle(Shape):

    def __init__(self, x=0, y=0, radius=5):

        self.x=x #this will store the final x - coordinate

        self.y=y #this will store the final y - coordinate

        self.radius=radius #this will store the final radius

        self.initial_figure=[x,y,1]

        self.initial_figure=np.array(self.initial_figure)

        self.ini_circle=self.initial_figure

        self.ini_radius=float(str(self.radius)[:]) #preventing aliasing

        self.ini_circle=np.array(self.ini_circle)


    def translate(self, dx, dy):

        self.ini_circle=self.initial_figure[:] #preventing aliasing

        self.ini_radius=float(str(self.radius)[:]) #preventing aliasing

        Shape.translate(self,dx,dy)

        B=np.transpose(self.initial_figure)

        self.initial_figure=np.dot(self.T_t,B)

        translate_x=round(self.initial_figure[0],2)

        translate_y=round(self.initial_figure[1],2)

        translate_radius=round(self.radius,2)

        return (translate_x,translate_y,translate_radius)


    def scale(self, sx):

        self.ini_circle=self.initial_figure[:] #preventing aliasing

        self.ini_radius=float(str(self.radius)[:]) #preventing aliasing

        self.radius=self.radius*sx #scaling my multiplying the scaling factor to radius

        scale_x=round(self.initial_figure[0],2)

        scale_y=round(self.initial_figure[1],2)

        scale_radius=round(self.radius,2)

        return (scale_x,scale_y,scale_radius)

    def rotate(self, deg, rx = 0, ry = 0):

        self.ini_circle=self.initial_figure[:]

        self.ini_radius=float(str(self.radius)[:])

        Shape.translate(self,-rx,-ry)

        C=np.transpose(self.initial_figure)

        self.initial_figure=np.dot(self.T_t,C)

        self.initial_figure=np.transpose(self.initial_figure)

        Shape.rotate(self,deg)

        D=np.transpose(self.initial_figure)

        self.initial_figure=np.dot(self.T_r,D)

        self.initial_figure=np.transpose(self.initial_figure)

        Shape.translate(self,rx,ry)

        E=np.transpose(self.initial_figure)

        self.initial_figure=np.dot(self.T_t,E)

        self.initial_figure=np.transpose(self.initial_figure)

        rotate_x=round(self.initial_figure[0],2)

        rotate_y=round(self.initial_figure[1],2)

        rotate_radius=round(self.radius,2)

        return (rotate_x,rotate_y,rotate_radius)


    def plot(self): #THIS Follows the Similar Algorithm as that of Polygon plot only difference being , in the end we do find x_dim= max of x coordinates + radius and same for y_dim

        self.initial_figure=np.transpose(self.initial_figure)

        self.ini_circle=np.transpose(self.ini_circle)

        ini_x_coordinate=self.ini_circle[0]

        ini_y_coordinate=self.ini_circle[1]

        ini_radius=self.ini_radius

        final_x_coordinate=self.initial_figure[0]

        final_y_coordinate=self.initial_figure[1]

        final_radius=self.radius

        self.initial_figure=np.transpose(self.initial_figure)

        self.initial_figure=np.transpose(self.initial_figure)

        self.initial_figure=np.transpose(self.initial_figure)

        self.ini_circle=np.transpose(self.ini_circle)


        circle_plot_x=np.array([])

        circle_plot_y=np.array([])

        circle_plot_x=np.append(circle_plot_x,ini_x_coordinate)

        circle_plot_x=np.append(circle_plot_x,final_x_coordinate)

        circle_plot_y=np.append(circle_plot_y,ini_y_coordinate)

        circle_plot_y=np.append(circle_plot_y,final_y_coordinate)

        circle_plot_x=np.absolute(circle_plot_x)

        circle_plot_y=np.absolute(circle_plot_y)

        max_x=np.amax(circle_plot_x)

        max_y=np.amax(circle_plot_y)

        circle_plot_radius=[]

        circle_plot_radius=np.array(circle_plot_radius)

        circle_plot_radius=np.append(circle_plot_radius,ini_radius)

        circle_plot_radius=np.append(circle_plot_radius,final_radius)

        max_radius = np.amax(circle_plot_radius)

        circle = plt.Circle((ini_x_coordinate, ini_y_coordinate), ini_radius, fill=False,linestyle = 'dashed')

        plt.gca().add_patch(circle)

        plt.axis('scaled')

        circle = plt.Circle((final_x_coordinate, final_y_coordinate), final_radius, fill=False  , linestyle = 'solid')

        plt.gca().add_patch(circle)

        plt.axis('scaled')

        Shape.plot(self,np.amax(circle_plot_radius)+max_x,np.amax(circle_plot_radius)+max_y)


if __name__ == "__main__":
    
    first=int(input('Enter first : 1 to plot and 0 otherwise'))
    
    tc=int(input('Please Enter the Number of Test Cases : '))

    for idx in range(tc):

    
        figure_type=int(input('Enter Type of Shape : 0 for Polygon and 1 for Circle '))
        
        if figure_type == 1:
       
            print('Circle is Chosen!')
       
            print('Enter x-coordinate of centre , y-coordinate of centre and radius')
       
            q,w,r=map(float,input().split())
       
            obj_a=Circle(q,w,r)
       
            print('Entered X-Coordinate is ',q)
       
            print('Entered Y-Coordinate is ' ,w)
       
            print('Entered Radius is ',r)
       
            queries=int(input('Please Enter the Number of Queries '))
       
            print('-'*40)
       
            print('1) R [Deg] [Rx] , R is Rotate')
       
            print('2) T [dx] [dy] , T is Translate')
       
            print('3) S [sx] [sy] , S is Scale')
       
            print('4) P , P is plot')
       
            print('-'*40)
       
            for i in range(queries):

                anime=input().split()

                if anime[0].lower()=='t':

                    print('Translate is Chosen')

                    if len(anime) == 2:

                        order_1=Circle.translate(obj_a,float(anime[1]),float(anime[1]))

                    elif len(anime) == 3:

                        order_1=Circle.translate(obj_a,float(anime[1]),float(anime[2]))

                    if first == 1:

                        print('G')

                        Circle.plot(obj_a)

                    elif first == 0:

                        obj_a.ini_radius == np.around(obj_a.ini_radius , decimals =2)

                        obj_a.ini_circle == np.around(obj_a.ini_circle , decimals=2)

                        tmp1=np.transpose(obj_a.ini_circle)

                        print('The Previous Plot is ')

                        print(tmp[0],tmp[1])

                        print('The Final Plot is ')

                        print(order_1[0],order_1[1],order_1[2])

                if anime[0].lower() =='s':

                    print('Scale is Chosen')

                    if len(anime) == 2:

                        order_3=Circle.scale(obj_a,float(anime[1]))

                    if first == 0:

                        obj_a.ini_radius = np.around(obj_a.ini_radius , decimals =2)

                        obj_a.ini_circle=np.around(obj_a.ini_circle , decimals = 2)

                        memo=np.transpose(obj_a.ini_circle)

                        print('Previous Plot is ')

                        print(memo[0],memo[1],obj_a.ini_radius)

                        print('Final Plot is ')

                        print(order_3[0],order_3[1],order_3[2])

                    elif first==1:

                        print('G')

                        Circle.plot(obj_a)

                if anime[0].lower() =='p':

                    print('Plot is Chosen')

                    Circle.plot(obj_a)

                if anime[0].lower() =='r':

                    print('Rotate is Chosen')

                    if len(anime) == 2:

                        order_2=Circle.rotate(obj_a,float(anime[1]))

                    elif len(anime) == 3:

                        order_2=Circle.rotate(obj_a,float(anime[1]),float(anime[1]))

                    elif len(anime) == 4:

                        order_2=Circle.rotate(obj_a,float(anime[1]),float(anime[2]))

                    if first == 0:

                        obj_a.ini_radius = np.around(obj_a.ini_radius , decimals =2)

                        obj_a.ini_circle=np.around(obj_a.ini_circle , decimals = 2)

                        memo=np.transpose(obj_a.ini_circle)

                        print('Previous Plot is ')

                        print(memo[0],memo[1],obj_a.ini_radius)

                        print('Final Plot is ')

                        print(order_2[0],order_2[1],order_2[2])

                    elif first==1:

                        print('G')

                        Circle.plot(obj_a)

        if figure_type==0:

            print('Polygon is chosen!')

            nos=int(input('Enter the Number of Sides of the Polygon'))

            print('Number of Sides chosen is ', nos)

            sides=[]

            for k in range(nos):


                tmp_side=list(map(int,input(f'Enter x{k+1} , y{k+1}').split()))

                tmp_side.append(1)

                sides.append(tmp_side)


            print('Your input Sides are ' , sides)

            tmp_obj=Polygon(sides)

            queries=int(input('Enter Number of Queries : '))

            print('Please Enter the Queries Below  : ')

            print('1) R [deg] [rx] (R:Rotate)')

            print('2) T [dx] (T:Translate)')

            print('3) S (sx) (sy) (S:Scale) ')

            print('4) P (P:Plot)')

            for m in range(queries):

                query_input=input().split()

                if query_input[0].lower() == 't':

                    if len(query_input) == 2:

                        Order_1=Polygon.translate(tmp_obj,float(query_input[1]),float(query_input[1]))

                    elif len(query_input)==3:

                        Order_1=Polygon.translate(tmp_obj,float(query_input[1]),float(query_input[2]))

                    if first==0:

                        tmp=np.transpose(tmp_obj.ini_polygon)

                        print('This is the Previous Plot Values')

                        print(tmp[0],tmp[1])

                        print('This is the New Plot Values')

                        print(Order_1[0],Order_1[1])

                    elif first==1:

                        Polygon.plot(tmp_obj)

                if query_input[0].lower() == 's':

                    if len(query_input) == 2:

                        Order_2=Polygon.scale(tmp_obj,float(query_input[1]),float(query_input[1]))

                    elif len(query_input)==3:

                        Order_2=Polygon.scale(tmp_obj,float(query_input[1]),float(query_input[2]))

                    if first==0:

                        tmp=np.transpose(tmp_obj.ini_polygon)

                        print('This is the Previous Plot Values')

                        print(tmp[0],tmp[1])

                        print('This is the New Plot Values')

                        print(Order_2[0],Order_2[1])

                    elif first==1:

                        Polygon.plot(tmp_obj)

                if query_input[0].lower()=='r':

                    if len(query_input) == 2:

                        Order_3=Polygon.rotate(tmp_obj,float(query_input[1]))

                    elif len(query_input)==3:

                        Order_3=Polygon.rotate(tmp_obj,float(query_input[1]),float(query_input[2]))

                    elif len(query_input) == 4:

                        Order_3=Polygon.rotate(tmp_obj,float(query_input[1]),float(query_input[2]),float(query_input[3]))

                    if first==0:

                        tmp=np.transpose(tmp_obj.ini_polygon)

                        print('This is the Previous Plot Values')

                        print(tmp[0],tmp[1])

                        print('This is the New Plot Values')

                        print(Order_3[0],Order_3[1])

                    elif first==1:

                        print('G')

                        Polygon.plot(tmp_obj)

                if query_input[0].lower()=='p':
                    Polygon.plot(tmp_obj)



#END OF ASSIGNMENT -3




