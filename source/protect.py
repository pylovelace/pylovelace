# -*- coding: utf-8 -*-
"""
PyLovelace
Copyright (c) 2023 PyLovelace
All rights reserved.

@Author: nshout
@File: protect.py
"""
import logging
import os
import shutil
import platform

from .kernel import PyLovelace, get_runtime_module, protect_code, compile_module, finalize

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)


class SingleMode:
    """
    PyLovelace single mode protection.
    """

    def __init__(
            self,
            file,
            clean: bool = False,
            anti_debug: bool = False,
            anti_module: bool = False,
            delay: int = 1,
            output_path: str = None,
            rename: bool = False,
            module: bool = False,
            hook: bool = False,
            remove_comments: bool = False,
            debug: bool = False
    ):
        self.file = file
        self.clean = clean
        self.anti_debug = anti_debug
        self.anti_module = anti_module
        self.delay = delay
        self.output_path = output_path
        self.rename = rename
        self.module = module
        self.hook = hook
        self.remove_comments = remove_comments
        self.debug = debug

    def generate(self):
        """
        Generate the protected file.
        :return:
        """
        logging.info("single mode")

        lovelace = PyLovelace(self.debug)

        input_dir = os.path.dirname(self.file)
        output_dir = os.path.join(input_dir, "dist")

        if self.output_path is not None:
            output_dir = self.output_path

        if self.clean:
            logging.info("clean set to True")
            if os.path.exists(output_dir):
                logging.info("cleaning dist folder")
                shutil.rmtree(output_dir)
                logging.info("cleaned dist folder")
            else:
                logging.warning("dist folder does not exist")
                logging.info("creating dist folder and skipping cleaning dist folder")

        os.makedirs(output_dir, exist_ok=True)

        # check if file is a python file and if it exists
        if not self.file.endswith(".py"):
            logging.error("file is not a python file")
            return

        if not os.path.exists(self.file):
            logging.error("file does not exist")
            return

        logging.info("started on file: " + self.file)

        with open(self.file, 'r', encoding='utf8') as f:
            __code = f.read()
            f.close()

        logging.info("reading file: " + os.path.basename(self.file))

        __secure_options = ", ".join(
            [
                str(self.anti_debug),
                str(self.anti_module),
                str(self.delay)
            ]
        )

        print(__secure_options)

        output_file = os.path.join(output_dir, os.path.basename(self.file))
        finalize(
            obfuscated_code=protect_code(
                __code,
                remove_comments=self.remove_comments,
                rename_functions_and_classes=self.rename,
                convert_pylovelace_comments=True,
                debug=self.debug,
                secure_options=__secure_options
            ),
            output_file=output_file,
            hook_mode=self.hook,
            module_mode=self.module
        )

        logging.info(f"anti debug set to: {self.anti_debug}")
        logging.info(f"anti module set to: {self.anti_module}")
        logging.info(f"delay set to: {self.delay}")

        if self.module:
            logging.info("compiling file: " + os.path.basename(self.file))
            compile_module(output_file)
            logging.info("compiled file: " + os.path.basename(self.file))

        if not os.path.exists(os.path.join(output_dir, "pylovelace_runtime")):
            os.makedirs(os.path.join(output_dir, "pylovelace_runtime"), exist_ok=True)

        runtime_folder = os.path.join(output_dir, "pylovelace_runtime")

        if platform.system() == 'Windows':
            get_runtime_module(os.path.join(runtime_folder, "pylovelace_runtime.pyd"))
        else:
            get_runtime_module(os.path.join(runtime_folder, "pylovelace_runtime.so"))

        with open(os.path.join(runtime_folder, "__init__.py"), "w") as f:
            f.write('''"""
pyintellect_runtime
"""
from .pylovelace_runtime import __ada__, __lovelace__''')

        logging.info("finished")
