from math import sin, cos, sqrt, atan2, radians

class Edge:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.coords = (latitude, longitude)

class Vertex:
    def __init__(self, edge1, edge2):
        self.edge1 = edge1
        self.edge2 = edge2
        self.length_longitude = edge1.longitude - edge2.length_longitude
        self.length_latitude = edge1.latitude - edge2.length_latitude
        self.length = R * 2 * atan2(sqrt(sin(self.length_latitude / 2)**2 + cos(edge1.latitude) * cos(edge2.latitude) * sin(
        self.length_longitude / 2) **2), sqrt(
        1 - sin(self.length_latitude / 2) ** 2 + cos(edge1.latitude) * cos(edge2.latitude) * sin(
        self.length_longitude / 2) **2))


def update(self, edge1):
    if all(not x for x in [edge1,edge2]):
        raise Exception('Must provide at least one edge to update')
    if edge1 and not edge2:
        return Vertex(edge1, edge2)
    elif edge2 and not edge1:
        return Vertex(self.edge1, edge2)
    else:
        return Vertex(edge1, edge2)

class Geofence:
    def __init__(self, vertices, lifetime):
        self.vertices = vertices
        self.lifetime = lifetime
        self.created_time = datetime.datetime.now()

    def is_expired(self):
        return datetime.datetime.now() - self.lifetime < self.created_time
        
