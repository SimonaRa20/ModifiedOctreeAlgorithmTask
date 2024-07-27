from fileutils import PointCloudUtils

def main():

    file_path = "2743_1234.las"

    # display data before run octree algorithm
    pcu = PointCloudUtils(file_path)
    pcu.read_file()
    pcu.display_points()

if __name__ == "__main__":
    main()
