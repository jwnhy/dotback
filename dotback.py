from pathlib import Path 
import tarfile
import json

def load_cfg_loc(path = "./cfgs/", file = "common.json"):
    full_path: str = Path(path, file)
    with open(full_path) as cfg_loc:
        return json.load(cfg_loc)

def save_cfg_tar(meta, target_folder = Path("~").expanduser(), tarname = "config.tar"):
    with tarfile.open(tarname, "w") as cfgtar:
        for folder in meta:
            name, path, cfgs = folder["name"], Path(folder["path"]).expanduser(), folder["files"]
            if path.is_relative_to(target_folder):
                for file in path.iterdir():
                    if file.name in cfgs:
                        cfgtar.add(file)

def restore_cfg_tar(target_folder = Path("~").expanduser(), tarname = "config.tar", dryrun = True):
    with tarfile.open(tarname, "r") as cfgtar:
        if not dryrun:
            for m in cfgtar.getmembers():
                if Path(m.path()).is_relative_to(target_folder):
                    m.name = m.name.removeprefix(target_folder)
                    cfgtar.extract(m, path=target_folder)
        else:
            cfgtar.list()

if __name__ == "__main__":
    save_cfg_tar(load_cfg_loc())
    restore_cfg_tar()
