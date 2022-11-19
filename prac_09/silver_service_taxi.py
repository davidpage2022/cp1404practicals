"""Silver service taxi exercise class"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi offering premium services"""

    def __init__(self, fanciness: float, **kwargs):
        """Construct a silver service taxi.

        :param fanciness: Factor for multiplying price per km."""
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __repr__(self):
        return str(vars(self))
