from measurement.base import BidimensionalMeasure

from measurement.measures.energy import Energy
from measurement.measures.time import Time


__all__ = [
    'EnergyRate'
]


class EnergyRate(BidimensionalMeasure):
    PRIMARY_DIMENSION = Energy
    REFERENCE_DIMENSION = Time

    ALIAS = {
        'W': 'J__s',
        'kW': 'kWh__hr',
        'btuh': 'Btu__hr',
        'Btuh': 'Btu__hr',
    }