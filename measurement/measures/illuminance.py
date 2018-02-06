from measurement.base import MeasureBase


__all__ = [
    'Illuminance',
]


class Illuminance(MeasureBase):
    STANDARD_UNIT = 'lux'
    UNITS = {
        'lux': 1.0,
        'fc': 0.09290304,
    }
    ALIAS = {
        'Lux': 'lux',
        'Foot-Candle': 'fc',
    }
    SI_UNITS = ['lux']

    def __init__(self, *args, **kwargs):
        super(Illuminance, self).__init__(*args, **kwargs)