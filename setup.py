#!/usr/bin/env python
# Copyright 2014-2020 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NAME = 'pyscf-dftd3'
DESCRIPTION  = 'DFT-D3 python interface'
SO_EXTENSIONS = {
}
DEPENDENCIES = ['pyscf', 'numpy']

#######################################################################
# Unless not working, nothing below needs to be changed.
metadata = globals()
import os
import sys
from setuptools import setup, find_namespace_packages, Extension
from setuptools.command.build_ext import build_ext
from distutils.errors import DistutilsExecError

topdir = os.path.abspath(os.path.join(__file__, '..'))
modules = find_namespace_packages(include=['pyscf.*'])
def guess_version():
    for module in modules:
        module_path = os.path.join(topdir, *module.split('.'))
        for version_file in ['__init__.py', '_version.py']:
            version_file = os.path.join(module_path, version_file)
            if os.path.exists(version_file):
                with open(version_file, 'r') as f:
                    for line in f.readlines():
                        if line.startswith('__version__'):
                            delim = '"' if '"' in line else "'"
                            return line.split(delim)[1]
    raise ValueError("Version string not found")
if not metadata.get('VERSION', None):
    VERSION = guess_version()


class CustomBuildExt(build_ext):
    def run(self):
        commands = '''
git clone https://github.com/cuanto/libdftd3
make -C libdftd3
mv libdftd3/lib/libdftd3.so pyscf/dftd3/
'''
        try:
            self.spawn(['bash', '-c', commands])
        except DistutilsExecError:
            self.warn('Failed to compile dftd3-lib')
            raise

from distutils.command.build import build
build.sub_commands = ([c for c in build.sub_commands if c[0] == 'build_ext'] +
                      [c for c in build.sub_commands if c[0] != 'build_ext'])

settings = {
    'name': metadata.get('NAME', None),
    'version': VERSION,
    'description': metadata.get('DESCRIPTION', None),
    'author': metadata.get('AUTHOR', None),
    'author_email': metadata.get('AUTHOR_EMAIL', None),
    'install_requires': metadata.get('DEPENDENCIES', []),
}
setup(
    include_package_data=True,
    packages=modules,
    ext_modules=[Extension('pyscf_lib_placeholder', [])],
    cmdclass={'build_ext': CustomBuildExt},
    **settings
)
