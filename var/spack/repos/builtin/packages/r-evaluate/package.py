# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvaluate(RPackage):
    """Parsing and Evaluation Tools that Provide More Details than the Default.

    Parsing and evaluation tools that make it easy to recreate the command
    line behaviour of R."""

    cran = "evaluate"

    version('0.15', sha256='885aee530a8b6aa7fd3acaa1ecd94ab58b71038c879ca37405f948e105907c5d')
    version('0.14', sha256='a8c88bdbe4e60046d95ddf7e181ee15a6f41cdf92127c9678f6f3d328a3c5e28')
    version('0.10.1', sha256='c9a763895d3f460dbf87c43a6469e4b41a251a74477df8c5d7e7d2b66cdd1b1c')
    version('0.10', sha256='6163baeb382c2c1e87d4e36a2e986ef74673d8a92ea8508c39ac662ff3519657')
    version('0.9',  sha256='e8118c9d6ec479c0e712913848404431b6b6c0282f3c131acaf9a677ab5fc6ae')

    depends_on('r@3.0.2:', type=('build', 'run'))

    depends_on('r-stringr@0.6.2:', type=('build', 'run'), when='@:0.11')
