#!/usr/bin/env python3
"""Test logthis as a component by generating a temporary Python script."""
import datetime
import io
import os
import pathlib
import subprocess
import sys
import tempfile
import textwrap
import unittest
import unittest.mock

import logthis

# pylint: disable=missing-class-docstring,missing-function-docstring,too-many-locals,no-self-use


class TestMocked(unittest.TestCase):
    def test_say(self) -> None:
        utcnow = datetime.datetime(1901, 12, 21)

        state = logthis.State()
        state.stdout = io.StringIO()
        state.stderr = io.StringIO()

        logthis.say("hello!", state=state, utcnow=utcnow)

        out = state.stdout.getvalue()
        expected_out = '\x1b[34mtest.py:    27: 1901-12-21 00:00:00Z:\x1b[0m hello!\n'
        self.assertEqual(expected_out, out)

        err = state.stderr.getvalue()
        expected_err = ''
        self.assertEqual(expected_err, err)

    def test_err(self) -> None:
        utcnow = datetime.datetime(1901, 12, 21)

        state = logthis.State()
        state.stdout = io.StringIO()
        state.stderr = io.StringIO()

        logthis.err("Wrong!", state=state, utcnow=utcnow)

        out = state.stdout.getvalue()
        expected_out = ''
        self.assertEqual(expected_out, out)

        err = state.stderr.getvalue()
        expected_err = '\x1b[31mtest.py:    44: 1901-12-21 00:00:00Z:\x1b[0m Wrong!\n'
        self.assertEqual(expected_err, err)


class TestComponent(unittest.TestCase):
    def test_say_and_err(self) -> None:
        text = textwrap.dedent('''\
            #!/usr/bin/env python3
            import logthis
            logthis.say("Hello!")
            logthis.err("Wrong.")
            ''')

        with tempfile.TemporaryDirectory() as tmpdir:
            pth = pathlib.Path(tmpdir) / "logthis_out.py"
            pth.write_text(text)

            proc = subprocess.Popen([sys.executable, str(pth)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
            if proc.returncode != 0:
                raise RuntimeError("Temporary script failed. Stdout:\n{!r}\nStderr:\n{!r}\n".format(out, err))

            name = pth.name

        ##
        # Check out
        ##

        expected_out_prefix = b'\x1b[34m' + name.encode() + b':     3: '
        # We need to ignore the datetime as this is too hard to mock.
        expected_out_suffix = b':\x1b[0m Hello!' + os.linesep.encode()

        self.assertTrue(out.startswith(expected_out_prefix))
        self.assertTrue(out.endswith(expected_out_suffix))

        self.assertEqual(len(expected_out_prefix) + 20 + len(expected_out_suffix), len(out))

        ##
        # Check err
        ##

        expected_err_prefix = b'\x1b[31m' + name.encode() + b':     4: '
        # We need to ignore the datetime as this is too hard to mock.
        expected_err_suffix = b':\x1b[0m Wrong.' + os.linesep.encode()

        self.assertTrue(err.startswith(expected_err_prefix))
        self.assertTrue(err.endswith(expected_err_suffix))

        self.assertEqual(len(expected_err_prefix) + 20 + len(expected_err_suffix), len(err))


if __name__ == "__main__":
    unittest.main()
