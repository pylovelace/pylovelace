"""
This file contains the configuration.
"""
version = "0.1.0"

docstring = f'''"""
PyIntellect
https://pyintellect.com
"""'''

start_code = """from pyintellect import __virtual__, __bootstrap__
__hook__(__file__)
__bootstrap__(__name__, {0}, {1})"""
