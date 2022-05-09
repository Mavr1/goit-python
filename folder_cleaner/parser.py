from pathlib import Path

EXTENSIONS = {'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
              'video': ('AVI', 'MP4', 'MOV', 'MKV'),
              'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
              'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
              'archives': ('ZIP', 'GZ', 'TAR')}


def parse_folder(path: Path):
    result: dict[str, list[str]] = {'images': [],
                                    'video': [],
                                    'documents': [],
                                    'audio': [],
                                    'archives': [],
                                    'unknown': []}

    folders_to_delete: list[Path] = []

    def rec(path: Path):
        for item in path.iterdir():
            if item.is_dir() and item.name not in result.keys():
                folders_to_delete.append(item)
                rec(item)
                continue

            extension = item.suffix[1:].upper()
            full_path = str(item.resolve())
            is_unknown = True

            for group, extensions in EXTENSIONS.items():
                if extension in extensions:
                    result[group].append(full_path)
                    is_unknown = False
                    break

            if is_unknown:
                result['unknown'].append(full_path)

    rec(path)

    return result, folders_to_delete
