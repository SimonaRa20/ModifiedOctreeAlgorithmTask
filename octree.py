import numpy as np

class SphereOctreeNode:
    def __init__(self, center, radius, points, depth, max_depth):
        self.center = center
        self.radius = radius
        self.points = points
        self.children = []
        self.depth = depth
        self.max_depth = max_depth

    def subdivide(self):
        # subdivide the node into 8 child nodes if the current depth is less than the maximum depth
        if self.depth >= self.max_depth:
            return
        
        # calculate new radius and child centers
        new_radius = self.radius / 2
        offsets = [np.array([dx, dy, dz]) * new_radius for dx in [-1, 1] for dy in [-1, 1] for dz in [-1, 1]]
        
        for offset in offsets:
            child_center = self.center + offset
            # filter points within the new sphere
            child_points = self.points_within_sphere(child_center, new_radius)
            if len(child_points) > 0:
                child_node = SphereOctreeNode(child_center, new_radius, child_points, self.depth + 1, self.max_depth)
                child_node.subdivide()
                self.children.append(child_node)
    
    def points_within_sphere(self, center, radius):
        # filter points to include only those within the sphere defined by the given center and radius
        distances = np.linalg.norm(self.points - center, axis=1)
        return self.points[distances <= radius]
