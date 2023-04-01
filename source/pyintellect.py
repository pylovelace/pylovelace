import argparse
import sys
from engine.configuration import *
from engine.single_mode import SingleMode


def _parse_args():
    """
    Parse arguments
    :return:
    """
    parse = argparse.ArgumentParser(
        prog='PyIntellect',
        description='PyIntellect Obfuscation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='%(prog)s [options]',
        epilog='''\
More information:
    https://pyintellect.com
'''
    )

    parse.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version}"
    )

    parse.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )

    obfuscation_parser = parse.add_argument_group(
        "Obfuscation",
        "Obfuscation options"
    )

    obfuscation_parser.add_argument(
        "-o",
        "--obfuscate",
        action="store",
        help="Obfuscate the input file"
    )

    obfuscation_parser.add_argument(
        "--mode",
        action="store",
        choices=["1", "2"],
        default="1",
        help="Obfuscation modes. 1 - One file, 2 - With modules"
    )

    obfuscation_parser.add_argument(
        "--output",
        action="store",
        help="Output directory"
    )

    registration_parser = parse.add_argument_group(
        "Registration",
        "Registration options"
    )

    registration_parser.add_argument(
        "-r",
        "--register",
        action="store",
        help="Register your license"
    )

    return parse


def _parse(initialized_arguments):
    """
    Parse arguments
    :param initialized_arguments:
    :return:
    """
    parser = _parse_args()
    arguments = parser.parse_args(initialized_arguments)
    if not initialized_arguments:
        parser.print_help()

    if arguments.obfuscate:
        if arguments.mode == "1":
            SingleMode(arguments.obfuscate).generate()
        elif arguments.mode == "2":
            raise NotImplementedError("Multi mode is not implemented yet")


def main():
    """
    Main function
    :return:
    """
    print(
        f"PyIntellect v{version}\n"
        f"Python v{sys.version.split()[0]}\n"
    )
    _parse(sys.argv[1:])


if __name__ == "__main__":
    main()
