# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Interfaz principal",
    version="1.2",
    description="Programa simulador de examen de la materia metods numerios, acutal version posiblemete existan mas cambios",
    author="Castillo Estrada Angel Ariel, Adrian Peña Perez, Diego Eduardo Burciaga Hernandez, Moises Gomez Pineda",
    author_email="aaer.tablet@gmail.com",
    url="None",
    license="Estudianil",
    scripts=["interaz_principal.py"],
    console=["interaz_principal.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)