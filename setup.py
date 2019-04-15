#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="GMod-CLI",
    version="0.0.1",
    description="A CLI for managing a gmod server instance",
    author="Kai Frankenhaueser",
    author_email="kailijan@flauschig.net",
    url="https://kailijan.github.io/GMod-CLI/",
    packages=["gmod_cli"],
    test_suite="nose.collector",
    tests_require=["nose"]
)
