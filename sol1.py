import os
import numpy as np
import numpy.linalg as la
import mayavi.mlab as mlab
import itertools
import utils

import meshcut



def read_stl(stl_fname):
    import stl
    m = stl.mesh.Mesh.from_file(stl_fname)

    # Flatten our vert array to Nx3 and generate corresponding faces array
    verts = m.vectors.reshape(-1, 3)
    faces = np.arange(len(verts)).reshape(-1, 3)

    verts, faces = meshcut.merge_close_vertices(verts, faces)
    return verts, faces



if __name__ == '__main__':
    
    file_name = "assignment.STL.stl"
    verts, faces = read_stl(file_name)

    mesh = meshcut.TriangleMesh(verts, faces)
    

    def show(plane):
        P = meshcut.cross_section_mesh(mesh, plane)
        
        colors = [
            (0, 1, 1),
            (1, 0, 1),
            (0, 0, 1)
        ]

        if True:
            utils.trimesh3d(mesh.verts, mesh.tris, color=(1, 1, 1),
                            opacity=0.5, representation='wireframe')
            utils.show_plane(plane.orig, plane.n, scale=1, color=(1, 0, 0),
                             opacity=0.5)

            for p, color in zip(P, itertools.cycle(colors)):
                p = np.array(p)
                mlab.plot3d(p[:, 0], p[:, 1], p[:, 2], tube_radius=None,
                            line_width=3.0, color=color)
                mlab.show()
        return P

    ##
    height = int(input("Enter the z-height"))
    plane_orig = (0, 0, 0)
    plane_norm = (0, 0, height)
    plane = meshcut.Plane(plane_orig, plane_norm)
    P = show(plane)
    mlab.show()
    
    height = int(input("Enter the z-height"))
    plane_orig = (0, 0, 0)
    plane_norm = (0, 0, height)
    plane = meshcut.Plane(plane_orig, plane_norm)
    P = show(plane)
    mlab.show()
    
    height = int(input("Enter the z-height"))
    plane_orig = (0, 0, 0)
    plane_norm = (0, 0, height)
    plane = meshcut.Plane(plane_orig, plane_norm)
    P = show(plane)
    mlab.show()
    