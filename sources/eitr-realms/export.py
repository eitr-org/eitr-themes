#!/usr/bin/env python3
"""Rebuild artwork using the native masters and Eitr's shared export tools."""
import argparse
import os
from pathlib import Path
import runpy

SOURCES = Path(__file__).resolve().parent
STORE = SOURCES.parents[1]
EITR = Path(os.environ.get('EITR_CHECKOUT', STORE.with_name('eitr')))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', choices=('04', '05', '06', '07', '08', '13'))
    batch = parser.parse_args().batch
    if batch in ('04', '13'):
        shared = '04' if batch == '04' else '09'
        exporter = runpy.run_path(str(EITR / f'branding/sources/wallpapers/batch-{shared}/export.py'))
        parameters = dict(root=STORE, records_root=SOURCES / 'themes')
        if batch == '13':
            parameters['number'] = batch
        exporter['main'](**parameters)
    else:
        runpy.run_path(str(SOURCES / f'branding/sources/wallpapers/batch-{batch}/export.py'),
                       run_name='__main__')


if __name__ == '__main__':
    main()
