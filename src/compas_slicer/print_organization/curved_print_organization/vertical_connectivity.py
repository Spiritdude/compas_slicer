import compas
import compas_slicer
from compas.geometry import closest_point_on_polyline, distance_point_point, Polyline, Vector, normalize_vector, Point
import logging
from compas_slicer.geometry import Path, PrintPoint
import compas_slicer.utilities as utils
import progressbar
from compas_slicer.parameters import get_param

logger = logging.getLogger('logger')
__all__ = ['VerticalConnectivity']


class VerticalConnectivity:
    """
    VerticalConnectivity finds the vertical relation between paths in a segment.
    It assumes that each path is supported by the path below, and the first path is
    supported by the BaseBoundary.
    This class creates PrintPoints and fills in their information.

    Attributes
    ----------
    paths : list of instances of compas_slicer.geometry.Path
    base_boundary : compas_slicer.print_organization.BaseBoundary
    mesh : compas.geometry.Mesh
    parameters : dict
    """

    def __init__(self, paths, base_boundary, mesh, parameters):
        assert isinstance(paths[0], compas_slicer.geometry.Path)
        assert isinstance(base_boundary, compas_slicer.print_organization.BaseBoundary)
        assert isinstance(mesh, compas.datastructures.Mesh)

        self.paths = paths
        self.base_boundary = base_boundary
        self.mesh = mesh
        self.parameters = parameters
        self.printpoints = {}  # dict with pne list of printpoints per path

    def __repr__(self):
        return "<VerticalConnectivity with %i paths>" % len(self.paths)

    ######################
    # Main
    def compute(self):
        pass
        # max_layer_height = get_param(self.parameters, key='max_layer_height', defaults_type='layers')
        # min_layer_height = get_param(self.parameters, key='min_layer_height', defaults_type='layers')
        #
        # all_pts = [pt for path in self.paths for pt in path.points]
        # closest_fks, projected_pts = utils.pull_pts_to_mesh_faces(self.mesh, all_pts)
        # normals = [Vector(*self.mesh.face_normal(fkey)) for fkey in closest_fks]
        #
        #
        # with progressbar.ProgressBar(max_value=len(self.paths)) as bar:
        #
        #     count = 0
        #     crv_to_check = Path(self.base_boundary.points, True)  # creation of fake path for the lower boundary
        #     for i, path in enumerate(self.paths):
        #         self.printpoints[i] = []
        #         for p in path.points:
        #             avg_layer_height = get_param(self.parameters, 'avg_layer_height', 'layers')
        #             cp = closest_point_on_polyline(p, Polyline(crv_to_check.points))
        #             d = distance_point_point(cp, p)
        #
        #             ppt = PrintPoint(pt=p, layer_height=avg_layer_height, mesh_normal=normals[count])
        #
        #             ppt.closest_support_pt = Point(*cp)
        #             ppt.distance_to_support = d
        #             ppt.layer_height = max(min(d, max_layer_height), min_layer_height)
        #             ppt.up_vector = Vector(*normalize_vector(Vector.from_start_end(cp, p)))
        #             ppt.frame = ppt.get_frame()
        #
        #             self.printpoints[i].append(ppt)
        #             count += 1
        #
        #         crv_to_check = path
        #
        #     bar.update(i)


if __name__ == "__main__":
    pass
