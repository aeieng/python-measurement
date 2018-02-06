from .base import MeasurementTestBase


from measurement.measures import EnergyRate


class EnergyRateTest(MeasurementTestBase):
    def test_W_to_Btu_kwarg(self):
        w = EnergyRate(W=1)
        btuh = EnergyRate(Btu__hr=3600.0/1055.05585)

        self.assertEqual(
            w.standard,
            btuh.standard,
        )