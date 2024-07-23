import unittest

from unittest.mock import patch  # Corrected import for mock

from test import LinkedList  # Assuming your code is in test.py

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        ll = LinkedList(1)
        ll.append(2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.lenth, 2)

    def test_print_ll(self):
        ll = LinkedList(1)
        ll.append(2)
        with unittest.mock.patch('builtins.print') as mocked_print:
            ll.print_ll()
            # Verify print was called correctly
            expected_calls = [unittest.mock.call(1, end=' '), unittest.mock.call("-->", end=' '),
                              unittest.mock.call(2, end=' '), unittest.mock.call("-->", end=' ')]
            self.assertEqual(mocked_print.mock_calls, expected_calls)


if __name__ == '__main__':
    unittest.main()