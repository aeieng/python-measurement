from measurement.base import MeasureBase


__all__ = [
    'HumidityRatio',
]


class HumidityRatio(MeasureBase):
    STANDARD_UNIT = 'kg__kg'
    UNITS = {
        'kg__kg': 1.0,
        'lb__lb': 1.0,
        'grain__lb': 0.00014285714,
    }
    ALIAS = {
        'Kilogram of Water Per Kilogram of Dry Air': 'kg__kg',
        'Pound of Water Per Pound of Dry Air': 'lb__lb',
        'Grain per Pound of Dry Air': 'grain__lb',
        'gr_lb': 'grain__lb',
    }
    SI_UNITS = ['kg__kg']

    def __init__(self, *args, **kwargs):
        super(HumidityRatio, self).__init__(*args, **kwargs)