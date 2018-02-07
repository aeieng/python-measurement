from measurement.base import MeasureBase


__all__ = [
    'Pressure',
]


class Pressure(MeasureBase):
    STANDARD_UNIT = 'Pa'
    UNITS = {
        'Pa': 1.0,
        "kPa": 1000.0,
        "psi": 6894.75728,
        "atm": 101325.0,
        "in_wg": 249.088908333,
        "in_hg": 3386.38866667,
        "ft_h20": 2989.0669
    }
    ALIAS = {
        'Pascal': 'Pa',
        'kiloPascal': 'kPa',
        'pound per square inch': 'psi',
        'lb__square_inch': 'psi',
        'lb__in2': 'psi',
        'atmosphere': 'atm',
        'inch water gauge': 'in_wg',
        'inch mercury': 'in_hg',
        'foot water': 'ft_h20',
    }
    SI_UNITS = ['Pa']

    def __init__(self, *args, **kwargs):
        super(Pressure, self).__init__(*args, **kwargs)
