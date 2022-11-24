"""Silver service taxi exercise class"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi offering premium services"""
    flagfall = 4.5

    def __init__(self, fanciness: float, **kwargs):
        """Construct a silver service taxi.

        :param fanciness: Factor for multiplying price per km."""
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip.
        Overrides Taxi.get_fare()"""
        return super().get_fare() + self.flagfall
