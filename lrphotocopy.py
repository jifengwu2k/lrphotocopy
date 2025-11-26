# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from __future__ import print_function

import argparse
import json
import os.path
import shutil
import sys
import time

import exifread


def get_image_datetime_from_exif(image_path):
    """
    Given an image file path, extract the shooting date from its EXIF metadata.
    Returns a time.struct_time object.
    Raises FileNotFoundError if the file does not exist.
    Raises KeyError if EXIF or date is missing.
    """
    with open(image_path, 'rb') as fp:
        tags = exifread.process_file(fp, details=False)
        for key in ('EXIF DateTimeOriginal', 'EXIF DateTimeDigitized', 'Image DateTime'):
            if key in tags:
                dt_string = str(tags[key])
                return time.strptime(dt_string, '%Y:%m:%d %H:%M:%S')
        raise KeyError('No suitable DateTime EXIF tag found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', required=False, action='store_true', help='verbose')
    parser.add_argument('-d', '--dry-run', required=False, action='store_true', help='dry run')

    parser.add_argument('source_dir', help='source directory')
    parser.add_argument('target_dir', help='target directory')
    args = parser.parse_args()

    source_directory = args.source_dir
    target_directory = args.target_dir
    is_verbose = args.verbose
    is_dry_run = args.dry_run

    for directory_path, directory_names, filenames in os.walk(source_directory):
        for filename in filenames:
            source_image_path = os.path.join(directory_path, filename)

            try:
                image_datetime = get_image_datetime_from_exif(source_image_path)

                year_directory = os.path.join(target_directory, '%04d' % image_datetime.tm_year)
                day_directory = os.path.join(
                    year_directory,
                    '%04d-%02d-%02d' % (image_datetime.tm_year, image_datetime.tm_mon, image_datetime.tm_mday)
                )
                target_image_path = os.path.join(day_directory, filename)

                if not is_dry_run:
                    if not os.path.isdir(target_directory):
                        os.mkdir(target_directory)

                    if not os.path.isdir(year_directory):
                        os.mkdir(year_directory)

                    if not os.path.isdir(day_directory):
                        os.mkdir(day_directory)

                    shutil.copy2(source_image_path, target_image_path)

                if is_dry_run or is_verbose:
                    print('%s -> %s' % (source_image_path, target_image_path))

            except (KeyError, IOError, OSError) as e:
                error_json = {
                    "image": source_image_path,
                    "exception": str(e)
                }

                print(json.dumps(error_json), file=sys.stderr)
