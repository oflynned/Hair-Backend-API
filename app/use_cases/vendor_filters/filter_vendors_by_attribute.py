from app.use_cases.vendor_filters.filter_exceptions import AttributeNotPresent, InvalidAttributeRange


class DistanceFilter:
    @staticmethod
    def get_vendors_within_distance(lat, lng, radius):
        if lat is None or lng is None or radius is None:
            raise AttributeNotPresent("Missing parameter for distance", 400)

        radius = int(radius)
        if radius < 500 or radius > 10_000:
            raise InvalidAttributeRange("Radius passed is out of range", 400)

        return "(" + str(lat) + ", " + str(lng) + ") search within " + str(radius) + "m"


class OpeningHoursFilter:
    pass


class CostFilter:
    pass


class StyleFilter:
    pass


class GenderFilter:
    pass
