from math import radians, sin, atan2, sqrt, cos


class Distance:
    @staticmethod
    def get_distance_between_points_in_km(x1, y1, x2, y2):
        r = 6373.0

        lat1 = radians(float(x1))
        lon1 = radians(float(y1))
        lat2 = radians(float(x2))
        lon2 = radians(float(y2))

        d_lon = lon2 - lon1
        d_lat = lat2 - lat1

        a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = r * c
        return round(distance, 2)
