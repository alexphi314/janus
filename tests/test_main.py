from unittest import TestCase
from collections import namedtuple
import six
if six.PY2:
    import mock
else:
    from unittest import mock

from janus.main import roll_die


class TestMain(TestCase):
    FakeDie = namedtuple("FakeDie", "roll")
    mock_mapping = {"d6": FakeDie(5)}

    @mock.patch("janus.main.parse_args", autospec=True)
    @mock.patch("janus.main.DIE_MAPPING", mock_mapping)
    def test_roll_die(self, mock_args):
        FakeArgs = namedtuple("FakeArgs", "die_type")
        mock_args.return_value = FakeArgs("d6")

        if six.PY2:
            with mock.patch("__builtin__.print", autospec=True) as mock_print:
                roll_die()
                mock_print.assert_called_with(5)
        else:
            with mock.patch("builtins.print", autospec=True) as mock_print:
                roll_die()
                mock_print.assert_called_with(5)
