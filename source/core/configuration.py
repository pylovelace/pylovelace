"""
This file contains the configuration.
"""
version = "0.0.4"

docstring = f'''"""
PyIntellect
https://pyintellect.com
"""'''

start_code = """from pyintellect import __virtual__, __bootstrap__
__virtual__(__name__, __file__)
__bootstrap__({0}, {1})"""

module_start_code = """__cc__ = {}
from pyintellect import __c__"""
