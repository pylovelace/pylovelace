"""
This file contains the configuration for the engine.
"""
version = "0.0.1a"

docstring = f'''"""
PyIntellect
https://pyintellect.com

version {version}
"""'''

start_code = """from pyintellect import __initiate__
__initiate__(__name__, __file__, {})"""

multi_start_code = """__code = {}
from pyintellect import __c__"""
