"""Unreliable car exercise"""
from random import randrange

from prac_09.car import Car


class UnreliableCar(Car):
    """Car that is unreliable (i.e. sometimes doesn't work)."""

    def __init__(self, reliability, **kwargs):
        """Construct an unreliable car.

        :param reliability: How reliable the car is as a percentage between 0 and 100."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the unreliable car.
        It has a chance of not driving any distance at all (returns 0),
        depending on the reliability."""
        if randrange(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
