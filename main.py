from pathlib import Path
import shutil
import sys
from parser import parse_folder
from normalize import normalize


def move_file(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)

    if target_folder.name == 'unknown':
        file_name.replace(target_folder / file_name.name)
        return

    name_to_normalize = file_name.name.replace(file_name.suffix, '')
    normalized_name = normalize(name_to_normalize) + file_name.suffix
    file_name.replace(target_folder / normalized_name)


def remove_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError as error:
        print(f'Check the {folder.name}. Looks like it\'s not empty')


def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    inner_folder_name = normalize(file_name.name.replace(file_name.suffix, ''))
    inner_folder = target_folder / inner_folder_name
    inner_folder.mkdir(exist_ok=True, parents=True)

    try:
        shutil.unpack_archive(str(file_name.resolve()),
                              str(inner_folder.resolve()))
    except shutil.ReadError:
        print(
            f'Something went wrong. Please check your archive file: {file_name.name}!')
        inner_folder.rmdir()
        return None

    file_name.unlink()


def main(folder: Path):
    files_data, folders_to_delete = parse_folder(folder)

    for target_folder_name, files_names in files_data.items():
        for file_name in files_names:
            if target_folder_name == 'archives':
                handle_archive(Path(file_name), folder / target_folder_name)
            else:
                move_file(Path(file_name), folder / target_folder_name)

    for folder_to_delete in folders_to_delete[::-1]:
        remove_folder(folder_to_delete)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please pass the folder name to be sorted out')

    folder_name = sys.argv[1]

    if folder_name:
        folder = Path(folder_name)
        print(f'Start in folder {folder.resolve()}')
        main(folder.resolve())
