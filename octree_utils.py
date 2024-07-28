import open3d as o3d
import numpy as np
from octree import SphereOctreeNode

def create_sphere_octree(points, max_depth = 4):
    # create a sphere-based octree from the given points
    if points is None:
        raise ValueError("Points data is not loaded.")
    
    # determine the bounding box of the point cloud
    min_bound = np.min(points, axis=0)
    max_bound = np.max(points, axis=0)
    center = (min_bound + max_bound) / 2
    radius = np.linalg.norm(max_bound - center)

    root_node = SphereOctreeNode(center, radius, points, 0, max_depth)
    root_node.subdivide()
    
    return root_node

def create_wireframe_sphere(center, radius):
    # create a wireframe sphere as a line
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=radius)
    sphere.compute_vertex_normals()
    lines = []

    # convert triangles to line segments
    for edge in sphere.triangles:
        lines.append([edge[0], edge[1]])
        lines.append([edge[1], edge[2]])
        lines.append([edge[2], edge[0]])

    # create a LineSet from the vertices and lines
    line_set = o3d.geometry.LineSet()
    line_set.points = sphere.vertices
    line_set.lines = o3d.utility.Vector2iVector(lines)
    line_set.translate(center)
    return line_set

def visualize_spheres(node, vis):
    # recursively add wireframe spheres for the given node and its children.
    if node is None:
        return
    
    wireframe_sphere = create_wireframe_sphere(node.center, node.radius)
    vis.add_geometry(wireframe_sphere)
    
    for child in node.children:
        visualize_spheres(child, vis)

def display_octree(root_node):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    visualize_spheres(root_node, vis)
    vis.run()
    vis.destroy_window()
