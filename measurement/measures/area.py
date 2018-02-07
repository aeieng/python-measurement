from measurement.base import MeasureBase


__all__ = [
    'Area',
]


class Area(MeasureBase):
    STANDARD_UNIT = 'square_meter'
    UNITS = {
        'square_meter': 1.0,
        'square_foot': 0.092903,
    }
    ALIAS = {
        'm2': 'square_meter',
        'square meter': 'square_meter',
        'ft2': 'square_meter',
        'square foot': 'square_foot',
    }
    SI_UNITS = ['square_meter']

    def __init__(self, *args, **kwargs):
        super(Area, self).__init__(*args, **kwargs)
