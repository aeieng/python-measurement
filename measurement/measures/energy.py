from measurement.base import MeasureBase


__all__ = [
    'Energy'
]


class Energy(MeasureBase):
    STANDARD_UNIT = 'J'
    UNITS = {
        'c': 4.18400,
        'C': 4184.0,
        'J': 1.0,
        'eV': 1.602177e-19,
        'tonne_tnt': 4184000000,
        'GJ': 1000000000.0,
        'kJ': 1000.0,
        'Wh': 3600.0,
        'kWh': 3600000.0,
        'Btu': 1055.05585,
        'kBtu': 1055055.85,
        'Therm': 105480400.0
    }
    ALIAS = {
        'joule': 'J',
        'calorie': 'c',
        'Calorie': 'C',
        'gigajoule': 'GJ',
        'kilojoule': 'kJ',
        'Watt-hour': 'Wh',
        'kilowatt-hour': 'kWh',
        'British Thermal Unit': 'Btu',
    }
    SI_UNITS = ['J', 'c', 'eV', 'tonne_tnt', 'GJ', 'kJ', 'Wh', 'kWh']
