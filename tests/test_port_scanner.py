
import argparse
import unittest

from port_scanner import parse_ports


class TestPortParsing(unittest.TestCase):

    def test_single_ports(self):
        self.assertEqual(
            parse_ports("22,80,443"),
            [22, 80, 443]
        )

    def test_port_range(self):
        self.assertEqual(
            parse_ports("80-83"),
            [80, 81, 82, 83]
        )

    def test_mixed_ports_and_ranges(self):
        self.assertEqual(
            parse_ports("22,80-82,443"),
            [22, 80, 81, 82, 443]
        )

    def test_duplicate_ports_are_removed(self):
        self.assertEqual(
            parse_ports("80,80,443"),
            [80, 443]
        )

    def test_invalid_port_is_rejected(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_ports("70000")

    def test_reversed_range_is_rejected(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_ports("100-80")


if __name__ == "__main__":
    unittest.main()
