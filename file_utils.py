import laspy
import numpy as np
import open3d as o3d

class PointCloudUtils:
    def __init__(self, file_path):
        self.file_path = file_path
        self.points = None

    def read_file(self):

        las = laspy.read(self.file_path)
        x = las.x
        y = las.y
        z = las.z
        
        self.points = np.vstack((x, y, z)).T

    def display_points(self):

        if self.points is None:
            raise ValueError("Points data is not loaded.")
        
        point_object = o3d.geometry.PointCloud()
        point_object.points = o3d.utility.Vector3dVector(self.points)
        
        render_object = o3d.visualization.Visualizer()
        render_object.create_window(width = 800, height = 800)
        render_object.add_geometry(point_object)

        render_object.run()
        render_object.destroy_window()
