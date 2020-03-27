#!/usr/bin/env python
"""
A generic wrapper to access nrn binaries from a python installation
Plese create a softlink with the binary name to be called.
"""
import os
import site
import subprocess as sp
import sys
import sysconfig


def _set_default_compiler():
    """Set (dont overwrite) CC/CXX so that apps dont use the build-time ones"""
    os.environ.setdefault("CC", sysconfig.get_config_var("CC"))
    os.environ.setdefault("CXX", sysconfig.get_config_var("CXX"))


def _launch_command(exe_name):
    NRN_PREFIX = os.path.join(site.getsitepackages()[0], 'neuron', '.data')
    os.environ["NEURONHOME"] = os.path.join(NRN_PREFIX, 'share/nrn')
    os.environ["NRNHOME"] = NRN_PREFIX
    exe_path = os.path.join(NRN_PREFIX, 'bin', exe_name)
    _set_default_compiler()

    return sp.call([exe_path] + sys.argv[1:])


if __name__ == '__main__':
    sys.exit(_launch_command(os.path.basename(sys.argv[0])))