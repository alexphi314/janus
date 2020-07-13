from unittest import TestCase
import six
if six.PY2:
    import mock
else:
    from unittest import mock

from janus.dice import HighVarianceD4, HighVarianceD6, HighVarianceD8, HighVarianceD10, HighVarianceD12, \
                       HighVarianceD20, HighVarianceD100


class TestDie(TestCase):
    @mock.patch("janus.dice.choice", autospec=True)
    def test_d4(self, mock_choice):
        mock_choice.return_value = 4

        self.assertEqual(4, HighVarianceD4().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d6(self, mock_choice):
        mock_choice.return_value = 5

        self.assertEqual(5, HighVarianceD6().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d8(self, mock_choice):
        mock_choice.return_value = 7

        self.assertEqual(7, HighVarianceD8().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d10(self, mock_choice):
        mock_choice.return_value = 9

        self.assertEqual(9, HighVarianceD10().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d12(self, mock_choice):
        mock_choice.return_value = 11

        self.assertEqual(11, HighVarianceD12().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d20(self, mock_choice):
        mock_choice.return_value = 19

        self.assertEqual(19, HighVarianceD20().roll)

    @mock.patch("janus.dice.choice", autospec=True)
    def test_d100(self, mock_choice):
        mock_choice.return_value = 90

        self.assertEqual(90, HighVarianceD100().roll)
