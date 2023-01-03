from cProfile import label
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

class com_scatter():
    def __init__(self):
        self.number_point=0
        self.frames=0
        self.x_max=0.0
        self.x_min=0.0
        self.y_max=0.0
        self.y_min=0.0
        self.z_max=0.0
        self.z_min=0.0
        self.elements=[]
        
    def max_min(self):        
        self.frames=int(len(self.new_array)/self.number_point)
        self.x_max=np.max(self.new_array[:,0])
        self.x_min=np.min(self.new_array[:,0])
        self.y_max=np.max(self.new_array[:,1])
        self.y_min=np.min(self.new_array[:,1])
        self.z_max=np.max(self.new_array[:,2])
        self.z_min=np.min(self.new_array[:,2])
        return self.x_min,self.x_max,self.y_min,self.y_max,self.z_min,self.z_max

    def three_dimension_scatter(self,file,number_points,elements):
        self.number_point=int(number_points)
        self.new_array=np.loadtxt(file,dtype=float)
        self.frames=int(len(self.new_array)/self.number_point)
        self.elements=elements
        print(self.elements)
        fig=plt.figure()
        plt.ion()
        for i in range(self.frames*3):
            fig.clf()
            fig.suptitle("3D scatter for com")
            ax1 = fig.add_subplot(111,projection='3d')

            ax1.scatter(self.new_array[self.number_point*i:self.number_point*(i+1),0],self.new_array[self.number_point*i:self.number_point*(i+1),1],self.new_array[self.number_point*i:self.number_point*(i+1),2])
            for j in range(self.number_point):
                print(self.elements[0])
                print(self.new_array[self.number_point*i+j,0],self.new_array[self.number_point*i+j,1],self.new_array[self.number_point*i+j,2])
                ax1.text(self.new_array[self.number_point*i+j,0],self.new_array[self.number_point*i+j,1],self.new_array[self.number_point*i+j,2],self.elements[j])


            ax1.set_xlabel("X")
            ax1.set_ylabel("Y")
            ax1.set_zlabel("Z")
            x_min,x_max,y_min,y_max,z_min,z_max=self.max_min()
            ax1.set_xlim(x_min,x_max)
            ax1.set_ylim(y_min,y_max)
            ax1.set_zlim(z_min,z_max)
            plt.pause(10)
        plt.ioff()
        plt.show()
        return
file=input('please input the File:')
number_points=input('please input the number of points:')
number_points=int(number_points)
elements=input('please input the noted elements:')
elements=elements.split(",")
three_dimension_scatter_instant=com_scatter()
three_dimension_scatter_instant.three_dimension_scatter(file,number_points,elements)


