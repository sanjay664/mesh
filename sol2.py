import numpy as np
import vtkplotlib as vpl
from stl import mesh
from matplotlib import pyplot as plt


if __name__ == '__main__':

    file_name = "assignment.STL.stl"
    def read_stl():
        return mesh.Mesh.from_file(file_name)

    def plot_stl(data):
        vpl.mesh_plot(data)
        vpl.show()
    

    #Read stl file
    data = read_stl()
    
    height = int(input("Enter the z-height"))
    points = data.vectors
    if(height == 10):
        front   = points[:,0,:]
    elif(height == 30):
        front   = points[:,1,:]
    elif(height == 50):
        front   = points[:,2,:]
    plt.plot(front)
    plt.show()
