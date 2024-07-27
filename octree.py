import open3d as o3d

def create_octree(points, max_depth=4):
    if points is None:
        raise ValueError("Points data is not loaded.")
    
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    
    # create the octree
    octree = o3d.geometry.Octree(max_depth=max_depth)
    octree.convert_from_point_cloud(point_cloud, size_expand=0.01)
    
    return octree

def display_octree(octree):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(octree)
    vis.run()
    vis.destroy_window()
