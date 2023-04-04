import argparse
import os
import sys
from engine.configuration import *
from engine.single_mode import SingleMode
from engine.module_mode import ModuleMode

# anti debug (pdb, pydev debugger)
# def check_if_debug() -> Callable[[FrameType, str, Any], Callable[[FrameType, str, Any], Any] | None] | None:
#     with suppress(AttributeError):
#         return sys.gettrace()
# if it's not none, then it runs in debug mode

def _parse_args():
    """
    Parse arguments
    :return:
    """
    parse = argparse.ArgumentParser(
        prog='PyIntellect',
        description='Pro License (Alpha State)',
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
        "(*) = Recommended\n"
        "(β) = Beta (Testing, not recommended)\n"
        "(α) = Alpha (Development, not recommended, might get removed)\n"
    )

    obfuscation_parser.add_argument(
        "-o",
        "--obfuscate",
        action="store",
        help="The file to obfuscate and download the required runtime module.",
        metavar="FILE"
    )

    obfuscation_parser.add_argument(
        "--mode",
        action="store",
        choices=["1", "2"],
        default="1",
        help="Obfuscation modes. \n"
             "1 - One file (Most secure), "
             "2 - Initiation file and all modules get obfuscated and modules get compiled."
    )

    obfuscation_parser.add_argument(
        "--module",
        action="store_true",
        help="Obfuscate and compile a module"
    )

    obfuscation_parser.add_argument(
        "--anti-debug",
        action="store_true",
        help="Python debugger check (*)"
    )

    obfuscation_parser.add_argument(
        "--anti-module",
        action="store_true",
        help="Anti debugger modules (β)"
    )

    obfuscation_parser.add_argument(
        "--anti-injection",
        action="store_true",
        help="Kernel injection check (α)"
    )

    obfuscation_parser.add_argument(
        "--anti-breakpoint",
        action="store_true",
        help="Kernel breakpoint check (α)"
    )

    obfuscation_parser.add_argument(
        "--delay",
        action="store",
        default=1,
        help="Check delay in seconds, default is 1"
    )

    obfuscation_parser.add_argument(
        "--output",
        action="store",
        help="Output directory"
    )

    registration_parser = parse.add_argument_group(
        "Registration",
    )

    registration_parser.add_argument(
        "-r",
        "--register",
        action="store",
        help="Register your license",
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
            ModuleMode(
                file=arguments.obfuscate,
                anti_debug=arguments.anti_debug,
                anti_module=arguments.anti_module,
                anti_injection=arguments.anti_injection,
                anti_breakpoint=arguments.anti_breakpoint,
            ).generate()
        elif arguments.mode == "1":
            SingleMode(
                arguments.obfuscate
            ).generate()
        elif arguments.mode == "2":
            raise NotImplementedError("Multi-mode obfuscation is not implemented yet.")


def main():
    """
    Main function
    :return:
    """
    print(
        f"PyIntellect v{version}\n"
        f"Python v{sys.version.split()[0]} (Supported)\n"
    )
    _parse(sys.argv[1:])


if __name__ == "__main__":
    main()
