# pip install cx_Freeze

import sys
from cx_Freeze import setup, Executable

# Para jogo com janela, no Windows evita abrir o terminal junto.
base = "gui" if sys.platform == "win32" else None

build_exe_options = {
    "packages": [
        "pygame",
        "pyttsx3",
        "tkinter",
        "json",
        "os",
        "time",
        "threading",
        "random",
        "datetime",
    ],
    "include_files": [
        ("assets", "assets"),
        ("recursos", "recursos"),
    ],
    "excludes": [
        "unittest",
        "email",
        "html",
        "http",
        "xml",
        "pydoc",
    ],
    "include_msvcr": True,
}

executaveis = [
    Executable(
        script="main.py",
        target_name="Jogo Homem-Aranha.exe",
        base=base,
        icon="assets/aranha.ico",
    )
]

setup(
    name="Jogo Homem-Aranha",
    version="1.0",
    description="Jogo 2D em Python com Pygame",
    options={
        "build_exe": build_exe_options
    },
    executables=executaveis,
)

# Para gerar a pasta build, use no terminal:
# python setup.py build