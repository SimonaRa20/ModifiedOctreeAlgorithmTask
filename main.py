from file_utils import PointCloudUtils
from octree_utils import create_sphere_octree, display_octree

def main():
    file_path = "2743_1234.las"
    max_depth = 2
    
    # display data before running the octree algorithm
    pcu = PointCloudUtils(file_path)
    pcu.read_file()
    pcu.display_points()
    
    # create and display the octree with spheres
    if pcu.points is not None:
        octree = create_sphere_octree(pcu.points, max_depth = max_depth)
        display_octree(octree)

if __name__ == "__main__":
    main()
