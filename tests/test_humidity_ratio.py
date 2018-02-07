from .base import MeasurementTestBase


from measurement.measures import HumidityRatio


class HumidityRatioTest(MeasurementTestBase):
    def test_humidity_ratio_kwarg(self):
        val1 = HumidityRatio(kg__kg=1.0)
        val2 = HumidityRatio(grain__lb=1.0/7000.0)

        self.assertEqual(
            round(val1.standard, 6),
            round(val2.standard, 6),
        )