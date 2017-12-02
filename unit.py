import unittest
import roman_cal

class TestCalc(unittest.TestCase):

    def test_rom_to_dec(self):
        result =roman_cal.rom_to_dec('XX')
        self.assertEquals(result,20)
    def test_dec_to_rom2(self):
        result2 =roman_cal.dec_to_rom2(10)
        self.assertEquals(result2,'X')
    def test_find(self):
        result3 = roman_cal.find('X','X','*')
        self.assertEquals(result3,'C')

if __name__ == '__main__':
    unittest.main()
