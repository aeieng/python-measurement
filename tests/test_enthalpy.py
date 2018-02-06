from .base import MeasurementTestBase


from measurement.measures import Enthalpy


class EnthalpyTest(MeasurementTestBase):
    def test_enthalpy_kwarg(self):
        j__kg = Enthalpy(J__kg=1.0)
        btu__lb = Enthalpy(Btu__lb=(453.592/1055.05585)/1000.0)

        self.assertEqual(
            round(j__kg.standard, 6),
            round(btu__lb.standard, 6),
        )