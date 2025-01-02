from cx_Freeze import setup, Executable

setup(
    name="word_solitaire",
    version="1.0",
    description="use word to solitaire",
    executables=[Executable("word_solitaire.py")],
    options={
        "build_exe": {
            "packages": ["tkinter"],  # 包含额外的库
            "include_files": []  # 包含额外的文件
        },
    }
)