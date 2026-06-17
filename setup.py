# pip install cx_Freeze

import cx_Freeze


executaveis = [
    cx_Freeze.Executable(
        script="main.py",
        target_name="Jogo Homem-aranha.exe",
        icon="assets/icone.png"
    )
]


cx_Freeze.setup(
    name="Jogo Kélen",
    options={
        "build_exe": {
            "packages": [
                "pygame",
                "pyttsx3",
                "tkinter",
                "json",
                "os",
                "time",
                "threading",
                "random"
            ],
            "include_files": [
                "assets",
                "recursos"
            ]
        }
    },
    executables=executaveis
)


# Para gerar a pasta build, use no terminal:
# python setup.py build