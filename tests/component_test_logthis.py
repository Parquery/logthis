#!/usr/bin/env python3
"""
Test logthis as a component by generating a temporary Python script.
"""
import datetime
import subprocess
import sys

import temppathlib


def main() -> int:
    """
    executes the main routine.
    """
    with temppathlib.NamedTemporaryFile(mode="wt", prefix="logthis_temporary", suffix=".py") as tmp:
        tmp.file.write('#!/usr/bin/env python3\n'
                       'import logthis\n'
                       'logthis.say("Hello!")\n'
                       'logthis.err("Wrong.")\n')
        tmp.file.flush()
        tmp.file.close()

        tmp.path.chmod(0o700)

        proc = subprocess.Popen([tmp.path.as_posix()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError("Temporary script failed. Stdout:\n{}\nStderr:\n{}\n".format(out, err))

        name = tmp.path.name
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

        expected_out = b'\x1b[34m' + name.encode() + b':     3: ' + now.encode() + b':\x1b[0m Hello!\n'

        if out != expected_out:
            for i, (expected, got) in enumerate(zip(expected_out, out)):
                if expected != got:
                    arrow = " " * (10 + len("{}".format(out[:i - 1]))) + "^"
                    raise AssertionError("Unexpected STDOUT:\nExpected: {}\nBut got:  {}\n{}".format(
                        expected_out, out, arrow))

        expected_err = b'\x1b[31m' + name.encode() + b':     4: ' + now.encode() + b':\x1b[0m Wrong.\n'
        if err != expected_err:
            for i, (expected, got) in enumerate(zip(expected_err, err)):
                if expected != got:
                    arrow = " " * (10 + len("{}".format(err[:i - 1]))) + "^"
                    raise AssertionError("Unexpected STDERR:\nExpected: {}\nBut got:  {}\n{}".format(
                        expected_err, err, arrow))

        sys.stdout.write(expected_out.decode())
        sys.stderr.write(expected_err.decode())

    return 0


if __name__ == "__main__":
    sys.exit(main())
