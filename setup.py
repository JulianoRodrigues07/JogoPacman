import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="Pacl/icone.png")]

cx_Freeze.setup(
    name="Pacman",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Pack"]
                           }},
    executables=executables
)
