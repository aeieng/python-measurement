from .base import MeasurementTestBase


from measurement.measures import Pressure


class PressureTest(MeasurementTestBase):
    def test_enthalpy_kwarg(self):
        val1 = Pressure(Pa=101325.0)
        val2 = Pressure(psi=14.6959488)

        self.assertEqual(
            round(val1.standard, 0),
            round(val2.standard, 0),
        )