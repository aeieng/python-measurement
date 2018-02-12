from measurement.base import MeasureBase


__all__ = [
    'EnergyFlux',
]


class EnergyFlux(MeasureBase):
    STANDARD_UNIT = 'Wh__m2'
    UNITS = {
        'Wh__m2': 1.0,
        "kJ__m2":  0.277777778,
        "Wh__ft2": 10.7639104,
        "Btu__ft2": 3.15459075,
    }
    ALIAS = {
        'Wh__square_meter': 'Wh__m2',
        'Wh__square_foot': 'Wh__ft2',
        'Btu__square_foot': 'Btu__ft2',
    }
    SI_UNITS = ['Wh__m2']

    def __init__(self, *args, **kwargs):
        super(EnergyFlux, self).__init__(*args, **kwargs)
