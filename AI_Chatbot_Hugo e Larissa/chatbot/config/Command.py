import argparse
import sys


class Cmd:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', help="Displays the steps of the resolution")

    args = parser.parse_args()
