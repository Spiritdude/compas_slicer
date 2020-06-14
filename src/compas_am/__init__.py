"""
********************************************************************************
compas_am
********************************************************************************

.. currentmodule:: compas_am


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import os
import compas
import sys


__author__ = ["Mathias Bernhard"]
__copyright__ = ""
__license__ = "MIT License"
__email__ = "bernhard@arch.ethz.ch"
__version__ = "0.1.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))

# Check if package is installed from git
# If that's the case, try to append the current head's hash to __version__
try:
    git_head_file = compas._os.absjoin(HOME, '.git', 'HEAD')

    if os.path.exists(git_head_file):
        # git head file contains one line that looks like this:
        # ref: refs/heads/master
        with open(git_head_file, 'r') as git_head:
            _, ref_path = git_head.read().strip().split(' ')
            ref_path = ref_path.split('/')

            git_head_refs_file = compas._os.absjoin(HOME, '.git', *ref_path)

        if os.path.exists(git_head_refs_file):
            with open(git_head_refs_file, 'r') as git_head_ref:
                git_commit = git_head_ref.read().strip()
                __version__ += '-' + git_commit[:8]
except Exception:
    pass

from .utilities import *  # noqa: F401 E402 F403
from .fabrication import *  # noqa: F401 E402 F403
from .input import *  # noqa: F401 E402 F403
from .polyline_simplification import *  # noqa: F401 E402 F403
from .positioning import *  # noqa: F401 E402 F403
from .geometry import *  # noqa: F401 E402 F403
from .slicing import *  # noqa: F401 E402 F403
from .sorting import *  # noqa: F401 E402 F403


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]





