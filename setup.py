from cx_Freeze import setup, Executable
import os

path = "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]

executables = [Executable("main.py")]

setup(
    name="CatScape",
    version="1.0",
    description="Cat Scape app",
    options={"build_exe": {"packages": ["pygame"], "include_files": asset_list_completa}},
    executables=executables
)