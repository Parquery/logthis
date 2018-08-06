#!/usr/bin/env python3
"""
Make an example of how to use logthis.
"""
import sys

import logthis


def main() -> int:
    """
    Execute the main routine.
    """
    logthis.say("Hello!")
    logthis.err("Wrong.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
