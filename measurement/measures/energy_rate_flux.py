from measurement.base import BidimensionalMeasure

from measurement.measures.energy_rate import EnergyRate
from measurement.measures.area import Area


__all__ = [
    'EnergyRateFlux'
]


class EnergyRateFlux(BidimensionalMeasure):
    PRIMARY_DIMENSION = EnergyRate
    REFERENCE_DIMENSION = Area

    ALIAS = {
        'W__m2': 'W__square_meter',
        'Btuh__ft2': 'Btuh__square_foot',
        'Btuh__sqft': 'Btuh__square_foot',
    }