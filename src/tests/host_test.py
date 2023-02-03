import unittest

from fontTools.merge.util import current_time

from host import Hostname


class TestHostObject(unittest.TestCase):
    def test_build_host_with_one_host(self):
        test_line = '127.0.0.1 something.test'

        host = Hostname(current_line=test_line)
        self.assertEqual(host.address, '127.0.0.1')
        self.assertEqual(host.hostname, ['something.test'])

    def test_host_object_with_two_hosts(self):
        test_line = '127.0.0.1 something.test something2.test'

        host = Hostname(current_line=test_line)
        self.assertEqual(host.address, '127.0.0.1')
        self.assertEqual(host.hostname, ['something.test', 'something2.test'])

    def test_if_host_is_localhost(self):
        localhost = '127.0.0.1 something.test'
        not_localhost = '192.168.0.1 something.test'

        host_localhost = Hostname(current_line=localhost)
        host_not_localhost = Hostname(current_line=not_localhost)

        self.assertTrue(host_localhost.is_localhost)
        self.assertFalse(host_not_localhost.is_localhost)

    def test_identify_file_comments(self):
        test_line = '# 127.0.0.1 something.test'

        host = Hostname(current_line=test_line)
        self.assertEqual(host.is_commented, True)

        test_line = '127.0.0.1 something.test'
        host = Hostname(current_line=test_line)
        self.assertEqual(host.is_commented, False)


if __name__ == '__main__':
    unittest.main()
