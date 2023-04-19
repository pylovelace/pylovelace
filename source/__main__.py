# -*- coding: utf-8 -*-
"""
PyLovelace
Copyright (c) 2023 PyLovelace
All rights reserved.

@Author: nshout
@File: __main__.py
"""
import argparse
import os
import getpass

from .kernel import lovelace, validate
from .protect import SingleMode
from secrets import compare_digest


def protection_parser(subparser):
    """--------------------------------------------------------------------------------
most common commands:

protect the given file with pylovelace.
    usage: pylovelace protect [options] file

to protect a module that gets compiled with pylovelace, use the --module option
    usage: pylovelace protect --module [options] file
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
    https://pylovelace.com
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
authenticate your pylovelace license if you never did before.
    usage: pylovelace authenticate --register

    this will ask you for a license, username and password to register.

log in to your pylovelace account.
    usage: pylovelace authenticate --login

    this will ask you for your username and password and activate your device.
---------------------------------------------------------------------------------"""
    parser = subparser.add_parser(
        'authenticate',
        help="manage authentication and PyLovelace license",
        description=authentication_parser.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''\
more information:
    https://pylovelace.com
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
        help='redirect to the PyLovelace store to buy a license'
    )

    return parser


def version():
    """
    Print version and license information
    """
    print(validate(v=True))


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
                args.verbose
            )
        SingleMode(
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
            debug=args.verbose,
        ).generate()
    elif args.category == 'authenticate':
        if args.login:
            username = input('username: ')
            password = getpass.getpass('password: ')

            auth = lovelace._PyLovelaceAdaEngine()
            if auth.login(
                    username=username,
                    password=password,
                    home=True
            ) is True:
                print('successfully logged in')

        elif args.register:
            username = input('username: ')
            password = getpass.getpass('password: ')
            repeat_password = getpass.getpass('repeat password: ')
            if not compare_digest(password, repeat_password):
                print('passwords do not match')
                return
            license = input('license: ')

            auth = lovelace._PyLovelaceAdaEngine()
            if auth.register(
                    username=username,
                    password=password,
                    pylovelace_license=license
            ) is True:
                print('you can now log in with your credentials')

        elif args.buy:
            os.system('start https://pyintellect.sell.app/product/pylovelace')
            print('opened https://pyintellect.sell.app/product/pylovelace in the browser')
        else:
            authenticate_parser.print_help()
    else:
        parser.print_help()


def main():
    """
    Main function
    :return:
    """
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
        description='usage: pylovelace <category>'
    )

    protection_parser(subparser)
    main_parser(
        parser=parser,
        authenticate_parser=authentication_parser(subparser)
    )


if __name__ == "__main__":
    main()
