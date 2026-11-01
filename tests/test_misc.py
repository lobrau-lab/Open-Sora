import sys
from unittest.mock import MagicMock


class MockPackage(MagicMock):
    __path__ = []


sys.modules["numpy"] = MagicMock()
sys.modules["torch"] = MockPackage()
sys.modules["torch.nn"] = MockPackage()
sys.modules["torch.utils"] = MockPackage()
sys.modules["torch.utils.tensorboard"] = MagicMock()
sys.modules["torch.utils.data"] = MagicMock()
sys.modules["torch.distributed"] = MagicMock()
sys.modules["colossalai"] = MockPackage()
sys.modules["colossalai.cluster"] = MockPackage()
sys.modules["colossalai.cluster.dist_coordinator"] = MagicMock()
sys.modules["psutil"] = MagicMock()

import unittest

from opensora.utils.misc import format_duration


class TestFormatDuration(unittest.TestCase):
    def test_format_duration(self):
        self.assertEqual(format_duration(0), "0s")
        self.assertEqual(format_duration(59), "59s")
        self.assertEqual(format_duration(60), "1m")
        self.assertEqual(format_duration(61), "1m 1s")
        self.assertEqual(format_duration(3600), "1h")
        self.assertEqual(format_duration(3661), "1h 1m 1s")
        self.assertEqual(format_duration(86400), "1d")
        self.assertEqual(format_duration(90061), "1d 1h 1m 1s")
        self.assertEqual(format_duration(86401), "1d 1s")

        # Test negative durations
        self.assertEqual(format_duration(-1), "-1s")
        self.assertEqual(format_duration(-65), "-1m 5s")
        self.assertEqual(format_duration(-3600), "-1h")
        self.assertEqual(format_duration(-86400), "-1d")
        self.assertEqual(format_duration(-90061), "-1d 1h 1m 1s")


if __name__ == "__main__":
    unittest.main()
