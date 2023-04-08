# -*- coding: utf-8 -*-
"""
PyIntellect
Python Obfuscation Tool

Copyright 2023 PyIntellect

Author - nshout
"""
import argparse
import sys
import core


def _parse_args():
    """
    Parse arguments
    :return:
    """
    parse = argparse.ArgumentParser(
        prog='PyIntellect',
        description='Free License (Alpha State)',
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
        version=f"%(prog)s {core.version}"
    )

    parse.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )

    obfuscation_parser = parse.add_argument_group(
        "Obfuscation",
        "(*) = Recommended\n"
        "(β) = Beta\n"
        "(α) = Alpha\n"
    )

    obfuscation_parser.add_argument(
        "-o",
        "--obfuscate",
        action="store",
        help="The file to obfuscate and download the required runtime module",
        metavar="FILE"
    )

    obfuscation_parser.add_argument(
        "--mode",
        action="store",
        choices=["1"],
        default="1",
        help="Obfuscation category"
    )

    obfuscation_parser.add_argument(
        "--module",
        action="store_true",
        help="Obfuscate and compile a module"
    )

    obfuscation_parser.add_argument(
        "--rename",
        action="store_true",
        help="Rename functions and classes (β)"
    )

    obfuscation_parser.add_argument(
        "--anti-debug",
        action="store_true",
        help="Python debugger check (*)"
    )

    obfuscation_parser.add_argument(
        "--anti-module",
        action="store_true",
        help="Anti debugger modules (*)"
    )

    obfuscation_parser.add_argument(
        "--delay",
        action="store",
        default=1,
        help="Check delay in seconds (Default: 1)"
    )

    obfuscation_parser.add_argument(
        "--output",
        action="store",
        help="Output directory (Not implemented yet)"
    )

    registration_parser = parse.add_argument_group(
        "Registration",
    )

    registration_parser.add_argument(
        "-r",
        "--register",
        action="store",
        help="Register your license (Not implemented yet)",
        metavar="LICENSE"
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
        if arguments.module:
            core.ModuleMode(
                file=arguments.obfuscate
            ).generate()
        elif arguments.mode == "1":
            core.SingleMode(
                arguments.obfuscate,
                anti_debug=arguments.anti_debug,
                anti_module=arguments.anti_module,
                delay=arguments.delay,
                rename=arguments.rename,
            ).generate()


def main():
    """
    Main function
    :return:
    """
    print(
        f"PyIntellect v{core.version}\n"
        f"Python v{sys.version.split()[0]} (Supported)\n"
    )
    _parse(sys.argv[1:])


if __name__ == "__main__":
    main()
