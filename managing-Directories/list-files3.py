from pathlib import Path

basepath = Path('/tmp')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
