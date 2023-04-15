"""
This file contains the configuration.
"""
version = "2023.1.0"

docstring = f'''"""
PyIntellect
https://pyintellect.com
"""'''

start_code = """from pyintellect_runtime import __hook__, __pyintellect__
__hook__(__file__)
__pyintellect__(__name__, {0}, {1})"""

start_code_no_hook = """from pyintellect_runtime import __pyintellect__
__pyintellect__(__name__, {0}, {1})"""
