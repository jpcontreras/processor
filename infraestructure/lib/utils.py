class Utils:

    # ===== Parameters
    # *+latitude+:Float
    # *+longitude+:Floar
    # ===== Return:
    # +Boolean+
    @staticmethod
    def is_valid_coordinates(latitude, longitude):
        return latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180