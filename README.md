# PyIntellect
An upcoming tool for Python code obfuscation.
The usage will be via a command line interface.

## Already Implemented Features
- Single file obfuscation (currently limited to 5kb files until licenses are implemented)
- Module obfuscation (currently limited to 5kb files until licenses are implemented)

## Planned Features
- Multiple modes of obfuscation (single file, with modules, etc.)
- ~~Single file obfuscation will not change the file extension (e.g. .py -> .py), this way it can be run as a normal Python file.~~ Already implemented!
- ~~Obfuscate and compile modules to .so or .pyd files. It will be possible to import and utilize these files as normal Python modules.~~ Already implemented!
- Variable renaming, String encryption, Control flow, Function renaming (Partially implemented)
- Expire after a certain date
- Affordable license price (one-time payment)
- Only one license

## Specialities
- PyIntellect does not utilize exec() or eval() like other obfuscators do.
- PyIntellect preserves the __name__ attribute.
- PyIntellect obfuscated files have a significant speed boost compared to other obfuscators.

## Supported Python Versions
- Python 3.11 and 3.12 (soon) only as of now, as I am currently focusing myself on the latest versions of Python.

I am yet unsure if I will support older versions of Python.

## Supported Operating Systems
- Windows 10/11 only as of now.

## Installation
PyIntellect is not yet available for installation. 
It will be available for installation once it is released.

How it will be: `pip install pyintellect`

## Documentation
Documentation will be available on the [PyIntellect website](https://pyintellect.com). The website is currently under development.

## License
PyIntellect's use will be put under purchasable licenses. The license will be a one-time payment, and will be valid for all future updates of PyIntellect.

The price of the license will be determined by the amount of features that are available at the time of purchase.

There will be a free version of PyIntellect, but it will be limited to a single mode of obfuscation, and will not be able to obfuscate modules and bigger projects.

PyIntellect is meant for commercial use, and it's core will be closed source. The core will be the part that will be responsible for the obfuscation process, and will be the part that will be licensed.