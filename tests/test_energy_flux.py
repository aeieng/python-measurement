from .base import MeasurementTestBase


from measurement.measures import EnergyFlux


class EnergyFluxTest(MeasurementTestBase):
    def test_Wh__m2_to_Btu__ft2_kwarg(self):
        val1 = EnergyFlux(Wh__m2=1.0)
        val2 = EnergyFlux(Btu__ft2=1.0/3.15459075)

        self.assertEqual(
            round(val1.standard, 4),
            round(val2.standard, 4),
        )