from .base import MeasurementTestBase


from measurement.measures import EnergyRateFlux


class EnergyRateTest(MeasurementTestBase):
    def test_W_to_Btu_kwarg(self):
        w__sqft = EnergyRateFlux(W__m2=1)
        btuh__sqft = EnergyRateFlux(Btuh__sqft=3600.0/1055.05585*0.0929035)

        self.assertEqual(
            round(w__sqft.standard, 4),
            round(btuh__sqft.standard, 4),
        )