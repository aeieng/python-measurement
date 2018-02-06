from measurement.base import BidimensionalMeasure

from measurement.measures.energy import Energy
from measurement.measures.mass import Mass


__all__ = [
    'Enthalpy'
]


class Enthalpy(BidimensionalMeasure):
    PRIMARY_DIMENSION = Energy
    REFERENCE_DIMENSION = Mass