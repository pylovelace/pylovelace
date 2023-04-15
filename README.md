# PyIntellect
A Python code obfuscation tool.
The usage will be via a command line interface.

## Features
- Single file obfuscation (currently limited to 5kb files until licenses are implemented)
- Module obfuscation (currently limited to 5kb files until licenses are implemented)
- Remove all comments
- Anti Python debugger
- Anti importing debugging packages
- Rename functions and classes
- Turn comments starting with `# pyintellect` into code. E.g. `# pyintellect print("test")` turns into `print("test")`.

## Planned Features / To Do
- Multiple modes of obfuscation (single file, with modules, etc.)
- Expire after a certain date

## Specialities
- PyIntellect preserves the __name\_\_ attribute.
- PyIntellect obfuscated files have a significant speed boost compared to other obfuscators.

## Supported Python Versions
- Python 3.11 only as of now, as I am currently focusing myself on the latest versions of Python.
- Python 3.12 soon
- Python 3.10 soon

## Supported Operating Systems
- Windows 10/11 only as of now.
- Linux soon.

## Installation

PyIntellect can be installed via pip:
`pip install pyintellect`

## Documentation
Documentation will be available on the [PyIntellect website](https://pyintellect.com). The website is currently under development.

## License
PyIntellect can be purchased over at: https://pyintellect.sell.app/product/pyintellect
PyIntellect can be used without a license, but a 5KB file limit will apply.
