# -*- coding: utf-8 -*-
"""
PyIntellect
Python Obfuscation Tool

Copyright 2023 PyIntellect

Author - nshout
"""
import argparse
import os
import sys
import core
import pwinput

from core.authentication import PyIntellectAuthentication


def protection_parser(subparser):
    """--------------------------------------------------------------------------------
most common commands:

protect the given file with pyintellect.
    usage: pyintellect protect [options] file

to protect a module that gets compiled with pyintellect, use the --module option
    usage: pyintellect protect --module [options] file
--------------------------------------------------------------------------------
(*) = recommended
(β) = beta
(α) = alpha
--------------------------------------------------------------------------------"""
    parser = subparser.add_parser(
        'protect',
        aliases=["protection"],
        help="manage protection and runtime modules",
        description=protection_parser.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''\
more information:
    https://pyintellect.com
'''
    )
    parser.add_argument(
        'file',
        help='.py file to protect'
    )

    parser.add_argument(
        "-o",
        "--output",
        action="store",
        help="output directory",
        metavar="PATH"
    )

    parser.add_argument(
        "--clean",
        action="store_true",
        help="clean the output directory",
        default=False,
    )

    protect_parser = parser.add_argument_group(
        "protection options",
    )

    protect_parser.add_argument(
        "--mode",
        action="store",
        choices=["1"],
        default="1",
        help="""
            protection/obfuscation mode
            (1 = standard mode)
            """
    )

    protect_parser.add_argument(
        "--hook",
        action="store_true",
        help="hook the protected file against changes (*)",
    )

    protect_parser.add_argument(
        "--hook-imports",
        action="store_true",
        help="hook all imports",
    )

    protect_parser.add_argument(
        "--strict-imports",
        action="store_true",
        help="prevent importing of not obfuscated modules",
    )

    protect_parser.add_argument(
        "--rename",
        action="store_true",
        help="rename functions and classes",
    )

    protect_parser.add_argument(
        "--anti-debug",
        action="store_true",
        help="anti Python debugger (*)"
    )

    protect_parser.add_argument(
        "--anti-module",
        action="store_true",
        help="anti debugger modules (*)"
    )

    protect_parser.add_argument(
        "--delay",
        action="store",
        default=1,
        help="(--anti) check delay in seconds (default: 1)",
        metavar="SECONDS"
    )

    removal_parser = parser.add_argument_group(
        "removal options",
    )

    removal_parser.add_argument(
        "--remove-docstrings",
        action="store_true",
        help="remove docstrings",
    )

    removal_parser.add_argument(
        "--remove-comments",
        action="store_true",
        help="remove comments (*)",
    )

    special_parser = parser.add_argument_group(
        "special options",
    )

    special_parser.add_argument(
        "--module",
        action="store_true",
        help="compile a module",
    )

    return parser


def authentication_parser(subparser):
    """---------------------------------------------------------------------------------
authenticate your pyintellect license if you never did before.
    usage: pyintellect authenticate --register

    this will ask you for a license, username and password to register.

log in to your pyintellect account.
    usage: pyintellect authenticate --login

    this will ask you for your username and password and activate your device.
---------------------------------------------------------------------------------"""
    parser = subparser.add_parser(
        'authenticate',
        help="manage authentication and PyIntellect license",
        description=authentication_parser.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''\
more information:
    https://pyintellect.com
'''
    )

    parser.add_argument(
        '--login',
        action='store_true',
        help='log into your account'
    )

    parser.add_argument(
        '--register',
        action='store_true',
        help='register a new account'
    )

    parser.add_argument(
        '--buy',
        action='store_true',
        help='redirect to the PyIntellect store to buy a license'
    )

    return parser


def version():
    """
    Print version and license information
    """
    auth = PyIntellectAuthentication()
    print(auth.get_info())


def main_parser(
        parser,
        authenticate_parser
):
    """
    Main parser
    """
    args = parser.parse_args()

    if args.version:
        version()
    elif args.category == 'protect':
        if args.verbose:
            print(
                args.file,
                args.clean,
                args.anti_debug,
                args.anti_module,
                args.delay,
                args.output,
                args.rename,
                args.module,
                args.hook,
                args.remove_comments,
                args.remove_docstrings,
                args.verbose,
            )
        core.SingleMode(
            file=args.file,
            clean=args.clean,
            anti_debug=args.anti_debug,
            anti_module=args.anti_module,
            delay=args.delay,
            output_path=args.output,
            rename=args.rename,
            module=args.module,
            hook=args.hook,
            remove_comments=args.remove_comments,
            remove_docstrings=args.remove_docstrings,
            debug=args.verbose,
        ).generate()
    elif args.category == 'authenticate':
        if args.login:
            username = input('username: ')
            password = pwinput.pwinput('password: ')

            auth = PyIntellectAuthentication()
            auth.login(
                username=username,
                password=password
            )

        elif args.register:
            username = input('username: ')
            password = pwinput.pwinput('password: ')
            repeat_password = pwinput.pwinput('repeat password: ')
            if password != repeat_password:
                print('passwords do not match')
                return
            license = input('license: ')

            auth = PyIntellectAuthentication()
            if auth.register(
                    username=username,
                    password=password,
                    pyintellect_license=license
            ):
                print('you can now log in with your credentials')

        elif args.buy:
            os.system('start https://pyintellect.sell.app/product/pyintellect')
            print('opened https://pyintellect.sell.app/product/pyintellect in the browser')
        else:
            authenticate_parser.print_help()
    else:
        parser.print_help()


def main():
    """
    Main function
    :return:
    """
    print(
        f"PyIntellect {core.version}\n"
        f"Python {sys.version.split()[0]}\n"
    )
    parser = argparse.ArgumentParser(
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="show version information and exit"
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='verbose output'
    )

    subparser = parser.add_subparsers(
        title='categories',
        dest='category',
        description='usage: pyintellect <category>'
    )

    protect_parser = protection_parser(subparser)
    authenticate_parser = authentication_parser(subparser)
    main_parser(
        parser=parser,
        authenticate_parser=authenticate_parser
    )


if __name__ == "__main__":
    main()
