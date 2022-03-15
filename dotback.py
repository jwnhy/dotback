#!/usr/bin/python
from pathlib import Path 
import tarfile
import json
import argparse

def load_cfg_loc(path, file):
    full_path: str = Path(path, file)
    with open(full_path) as cfg_loc:
        return json.load(cfg_loc)

def save_cfg_tar(meta, target_folder, tarname):
    target_folder = Path(target_folder).expanduser()
    try:
        with tarfile.open(tarname, 'x') as cfgtar:
            for folder in meta:
                name, path, cfgs = folder['name'], Path(folder["path"]).expanduser(), folder["files"]
                if path.is_relative_to(target_folder):
                    for file in path.iterdir():
                        if file.name in cfgs:
                            print('[NEW] ' + str(file))
                            cfgtar.add(file)
    except FileExistsError as err:
        print(err)

def restore_cfg_tar(target_folder, tarname, dryrun):
    target_folder = Path(target_folder).expanduser()
    with tarfile.open(tarname, 'r') as cfgtar:
        for m in cfgtar.getmembers():
            abs_path = Path('/', m.path)
            if abs_path.is_relative_to(target_folder):
                m.name = m.name.removeprefix(target_folder.name)
                if dryrun:
                    print('[DRYRUN] ' + str(target_folder.joinpath(abs_path)))
                else:
                    print('[RESTORED] ' + str(target_folder.joinpath(abs_path)))
                    cfgtar.extract(m, path=target_folder)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dot Configuration File Backup Tool')
    subparsers = parser.add_subparsers()

    parser_r = subparsers.add_parser('restore', help='restore configs', aliases=['r'])
    parser_r.add_argument('--tar', metavar='T', type=str, default='config.tar',
            help='the tarfile to be restored from [default: config.tar]')
    parser_r.add_argument("--actual", action='store_true', default=False,
            help='whether to actually write to disk [default: False]')
    parser_r.add_argument('--prefix', metavar='P', type=str, default='~',
            help='path-prefix to restore to [default: ~]')

    parser_s = subparsers.add_parser('save', help='save configs', aliases=['s'])
    parser_s.add_argument('--folder', metavar='V', type=str, default='./cfgs/',
            help='the folder where preset jsons are [default: ./cfgs/]')
    parser_s.add_argument('--cfg', metavar='C', type=str, default='common.json',
            help='the preset json to use [default: common.json]')
    parser_s.add_argument('--output', metavar='O', type=str, default='config.tar',
            help='output tarfile path [default: config.tar]')
    parser_s.add_argument('--prefix', metavar='P', type=str, default='~',
            help='path-prefix to save from [default: ~]')
    
    args = parser.parse_args()
    if len(args.__dict__) <= 1:
        parser.print_help()
        print()
        parser_s.print_help()
        print()
        parser_r.print_help()
    elif args.__dict__.get('tar') is not None:
        dryrun = not args.actual
        restore_cfg_tar(args.prefix, args.tar, dryrun)
    elif args.__dict__.get('cfg') is not None:
        meta = load_cfg_loc(args.folder, args.cfg)
        save_cfg_tar(meta, args.prefix, args.output)
