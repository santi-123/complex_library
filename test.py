import libreria as lc
import unittest
import math


class Test_operatios_complex(unittest.TestCase):

    def test_sum(self):
        # Prueba de aceptación
        sum = lc.suma((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(sum[0], 0.4)
        self.assertAlmostEqual(sum[1], 11.8)

        # Prueba de negación
        sum_neg = lc.suma((3, 5), (-2.6, 6.8))
        self.assertNotAlmostEqual(sum_neg[0], 1.4)
        self.assertNotAlmostEqual(sum_neg[1], 10.8)

    def test_sum2(self):
        # Prueba de aceptación
        sum = lc.suma((3, 2), (-5, 5.2))
        self.assertAlmostEqual(sum[0], -2)
        self.assertAlmostEqual(sum[1], 7.2)

        # Prueba de negación
        sum_neg = lc.suma((3, 2), (-5, 5.2))
        self.assertNotAlmostEqual(sum_neg[0], 0)
        self.assertNotAlmostEqual(sum_neg[1], 6.2)

    def test_rest(self):
        # Prueba de aceptación
        rest = lc.resta((3, 2), (-5, 5.2))
        self.assertAlmostEqual(rest[0], 8)
        self.assertAlmostEqual(rest[1], -3.2)

        # Prueba de negación
        rest_neg = lc.resta((3, 2), (-5, 5.2))
        self.assertNotAlmostEqual(rest_neg[0], 7)
        self.assertNotAlmostEqual(rest_neg[1], -2.2)

    def test_rest2(self):
        # Prueba de aceptación
        rest = lc.resta((9, 5), (-5, 5.2))
        self.assertAlmostEqual(rest[0], 14)
        self.assertAlmostEqual(rest[1], -0.2)

        # Prueba de negación
        rest_neg = lc.resta((9, 5), (-5, 5.2))
        self.assertNotAlmostEqual(rest_neg[0], 15)
        self.assertNotAlmostEqual(rest_neg[1], 0)

    def test_mult(self):
        # Prueba de aceptación
        mult = lc.producto((3, 2), (-5, 5.2))
        self.assertAlmostEqual(mult[0], -25.4)
        self.assertAlmostEqual(mult[1], 5.6)

        # Prueba de negación
        mult_neg = lc.producto((3, 2), (-5, 5.2))
        self.assertNotAlmostEqual(mult_neg[0], -24.4)
        self.assertNotAlmostEqual(mult_neg[1], 6.6)

    def test_mult2(self):
        # Prueba de aceptación
        mult = lc.producto((9, 5), (-5, 5.2))
        self.assertAlmostEqual(mult[0], -71)
        self.assertAlmostEqual(mult[1], 21.800000000000004)

        # Prueba de negación
        mult_neg = lc.producto((9, 5), (-5, 5.2))
        self.assertNotAlmostEqual(mult_neg[0], -70)
        self.assertNotAlmostEqual(mult_neg[1], -20.8)

    def test_div1(self):
        # Prueba de aceptación
        div = lc.division((3, 2), (-5, 5.2))
        self.assertAlmostEqual(div[0], -0.08839354342813219)
        self.assertAlmostEqual(div[1], -0.49192928516525747)

        # Prueba de negación
        div_neg = lc.division((3, 2), (-5, 5.2))
        self.assertNotAlmostEqual(div_neg[0], -0.1)
        self.assertNotAlmostEqual(div_neg[1], -0.5)

    def test_div2(self):
        # Prueba de aceptación
        div = lc.division((9, 5), (-5, 5.2))
        self.assertAlmostEqual(div[0], -0.3651037663335895)
        self.assertAlmostEqual(div[1], -1.3797079169869333)

        # Prueba de negación
        div_neg = lc.division((9, 5), (-5, 5.2))
        self.assertNotAlmostEqual(div_neg[0], -0.36)
        self.assertNotAlmostEqual(div_neg[1], -1.37)

    def test_mod(self):
        # Prueba de aceptación
        self.assertAlmostEqual(lc.modulo((3, 2)), 3.605551275463989)

        # Prueba de negación
        self.assertNotAlmostEqual(lc.modulo((3, 2)), 3.7)

    def test_mod2(self):
        # Prueba de aceptación
        self.assertAlmostEqual(lc.modulo((9, 5)), 10.295630140987)

        # Prueba de negación
        self.assertNotAlmostEqual(lc.modulo((9, 5)), 10.3)

    def test_conj(self):
        # Prueba de aceptación
        conj = lc.conjugado((3, 2))
        self.assertEqual(conj, (3, -2))

        # Prueba de negación
        self.assertNotEqual(conj, (3, 2))

    def test_conj2(self):
        # Prueba de aceptación
        conj = lc.conjugado((9, 5))
        self.assertEqual(conj, (9, -5))

        # Prueba de negación
        self.assertNotEqual(conj, (9, 5))

    def test_car_pol(self):
        # Prueba de aceptación
        pol = lc.car_pol((3, 2))
        self.assertAlmostEqual(pol[0], 3.605551275463989)
        self.assertAlmostEqual(pol[1], 0.5880026035475675)

        # Prueba de negación
        self.assertNotAlmostEqual(pol[0], 3.6)
        self.assertNotAlmostEqual(pol[1], 0.59)

    def test_car_pol2(self):
        # Prueba de aceptación
        pol = lc.car_pol((9, 5))
        self.assertAlmostEqual(pol[0], 10.295630140987)
        self.assertAlmostEqual(pol[1], 0.507098504392337)

        # Prueba de negación
        self.assertNotAlmostEqual(pol[0], 10.3)
        self.assertNotAlmostEqual(pol[1], 0.51)

    def test_pol_car(self):
        # Prueba de aceptación
        car = lc.pol_car((3, math.pi / 6))
        self.assertAlmostEqual(car[0], 2.598076211353316)
        self.assertAlmostEqual(car[1], 1.5)

        # Prueba de negación
        car_neg = lc.pol_car((3, math.pi / 6))
        self.assertNotAlmostEqual(car_neg[0], 2.6)
        self.assertNotAlmostEqual(car_neg[1], 1.6)

    def test_pol_car2(self):
        # Prueba de aceptación
        car = lc.pol_car((9, math.pi / 3))
        self.assertAlmostEqual(car[0], 4.5)
        self.assertAlmostEqual(car[1], 7.794228634059947)

        # Prueba de negación
        car_neg = lc.pol_car((9, math.pi / 3))
        self.assertNotAlmostEqual(car_neg[0], 4.6)
        self.assertNotAlmostEqual(car_neg[1], 7.8)

    def test_fase(self):
        # Prueba de aceptación
        self.assertAlmostEqual(lc.fase((3, 2)), 0.5880026035475675)

        # Prueba de negación
        self.assertNotAlmostEqual(lc.fase((3, 2)), 0.6)

    def test_fase2(self):
        # Prueba de aceptación
        self.assertAlmostEqual(lc.fase((9, 5)), 0.507098504392337)

        # Prueba de negación
        self.assertNotAlmostEqual(lc.fase((9, 5)), 0.51)


if __name__ == '__main__':
    unittest.main()
