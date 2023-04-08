# PyIntellect
A CPythonic Python code obfuscation tool.
The usage will be via a command line interface.

## Already Implemented Features

- Single file obfuscation (currently limited to 5kb files until licenses are implemented)
- Module obfuscation (currently limited to 5kb files until licenses are implemented)
- Remove all comments
- Anti Python debugger
- Anti importing debugging packages
- Rename functions and classes
- Turn comments starting with `# pyintellect` into code. E.g. `# pyintellect print("test")` turns into `print("test")`.

## Planned Features / To Do
- Multiple modes of obfuscation (single file, with modules, etc.)
- Variable renaming, String encryption, Control flow, Function renaming (Partially implemented)
- Anti Python debugger
- Expire after a certain date
- Affordable license price (one-time payment)
- Only one license

## Specialities
- PyIntellect does not utilize exec(), eval() or lambda like other obfuscators do.
- PyIntellect preserves the __name\_\_ attribute.
- PyIntellect obfuscated files have a significant speed boost compared to other obfuscators.

## Supported Python Versions
- Python 3.11 and 3.12 (soon) only as of now, as I am currently focusing myself on the latest versions of Python.

I am yet unsure if I will support older versions of Python.

## Supported Operating Systems
- Windows 10/11 only as of now.
- Linux soon.

## Installation

PyIntellect can be installed via pip:
`pip install pyintellect`

## Documentation
Documentation will be available on the [PyIntellect website](https://pyintellect.com). The website is currently under development.

## License
PyIntellect's use will be put under purchasable licenses. The license will be a one-time payment, and will be valid for all future updates of PyIntellect.

The price of the license will be determined by the amount of features that are available at the time of purchase.

There will be a free version of PyIntellect, but it will be limited to a single mode of obfuscation, and will not be able to obfuscate modules and bigger projects.

PyIntellect is meant for commercial use, and it's core will be closed source. The core will be the part that will be responsible for the obfuscation process, and will be the part that will be licensed.
