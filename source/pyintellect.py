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
    parser = argparse.ArgumentParser(
        prog='PyIntellect',
        description='Free License (Alpha State)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='pyintellect [options]',
        epilog='''\
More information:
    https://pyintellect.com
'''
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {core.version}"
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )

    registration_parser = parser.add_argument_group(
        "Registration",
    )

    registration_parser.add_argument(
        "-r",
        "--register",
        action="store",
        help="Register your license (Not implemented yet)",
        metavar="LICENSE"
    )

    subparser = parser.add_subparsers(
        title="Categories",
        metavar="",
    )

    protection_parser(subparser)

    return parser


def protection_parser(subparser):
    """---------------------------------------------------------------------------------
Protect the given file with PyIntellect.
    usage: pyintellect protect [options] FILE

To protect a module that gets compiled with PyIntellect, use the --module option.
    usage: pyintellect protect --module [options] FILE
---------------------------------------------------------------------------------
(*) = Recommended
(β) = Beta
(α) = Alpha
---------------------------------------------------------------------------------"""
    parser = subparser.add_parser(
        "protect",
        aliases=["p", "protection"],
        help="Manage protection and runtime modules",
        description=protection_parser.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='pyintellect protect [options] FILE',
        epilog='''\
More information:
    https://pyintellect.com
'''
    )

    parser.add_argument(
        "-o",
        "--output",
        action="store",
        help="Output directory",
        metavar="PATH"
    )

    protect_parser = parser.add_argument_group(
        "Protection Options",
    )

    protect_parser.add_argument(
        "--mode",
        action="store",
        choices=["1"],
        default="1",
        help="""
        Protection/Obfuscation mode
        (1 = Standard mode)
        """
    )

    protect_parser.add_argument(
        "--hook",
        action="store_true",
        help="Hook the protected file against changes",
        default=True,
    )

    protect_parser.add_argument(
        "--hook-imports",
        action="store_true",
        help="Hook all imports",
        default=False,
    )

    protect_parser.add_argument(
        "--block-imports",
        action="store_true",
        help="Block importing of not obfuscated modules",
        default=False,
    )

    protect_parser.add_argument(
        "--rename",
        action="store_true",
        help="Rename functions and classes",
        default=False,
    )

    protect_parser.add_argument(
        "--anti-debug",
        action="store_true",
        help="Python debugger check (*)"
    )

    protect_parser.add_argument(
        "--anti-module",
        action="store_true",
        help="Anti debugger modules (*)"
    )

    protect_parser.add_argument(
        "--delay",
        action="store",
        default=1,
        help="(--anti) Check delay in seconds (Default: 1)",
        metavar="SECONDS"
    )

    removal_parser = parser.add_argument_group(
        "Removal Options",
    )

    removal_parser.add_argument(
        "--remove-docstrings",
        action="store_true",
        help="Remove docstrings",
        default=False,
    )

    removal_parser.add_argument(
        "--remove-comments",
        action="store_true",
        help="Remove comments (*)",
        default=False,
    )

    special_parser = parser.add_argument_group(
        "Special Options",
    )

    special_parser.add_argument(
        "--module",
        action="store_true",
        help="Compile a module",
        default=False,
    )

    if len(sys.argv) == 2:
        parser.print_help()
        sys.exit(1)


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
