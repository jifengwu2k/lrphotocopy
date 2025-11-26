# `lrphotocopy`

Organize and copy your photos into folders by shooting date, using Adobe Lightroom's year/date folder structure.

## Features

- **Lightroom-style folders:** Copies images into `<target>/<YEAR>/<YEAR-MM-DD>/` structure based on EXIF date.
- **Preserves file attributes** while copying.
- **Dry run** (`-d`): Preview actions without changing files.
- **Verbose** (`-v`): Detailed progress output.
- **Supported files:** `.jpg`, `.jpeg`, `.tif`, `.tiff`, `.png`, `.heic`.
- **Skips non-photos** and images without EXIF dates - with warnings.
- **Cross-platform:** Requires Python 2+.

## Installation

```shell
pip install lrphotocopy
```

## Usage

```shell
python -m lrphotocopy [options] <source_dir> <target_dir>
```

### Common Options

- `-v`, `--verbose` &nbsp;&nbsp; Show detailed output.
- `-d`, `--dry-run` &nbsp;&nbsp;&nbsp; Simulate actions, make no changes.

### Examples

Organize photos from `~/Pictures` into `~/LR_Organized` using Lightroom's convention:

```shell
python -m lrphotocopy -v ~/Pictures ~/LR_Organized
```

Dry run:

```shell
python -m lrphotocopy -v -d ~/Pictures ~/LR_Organized
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## About

**lrphotocopy** was created to quickly sort and back up photos into a Lightroom-style folder structure.