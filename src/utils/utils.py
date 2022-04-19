import os
import random
import numpy as np
import yaml
import torch


def setRandomSeed(seed=42):
    """Reproducer for pytorch experiment.
    Parameters
    ----------
    seed: int, optional (default = 2019)
        Radnom seed.
    Example
    -------
    setRandomSeed(seed=2019).
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.enabled = True


def printDash(num = 50):

    print(''.join(['-']*num))


def load_config(config_path="./config/config.yaml"):
    with open(config_path, "r") as F:
        yaml_data = yaml.safe_load(F)
    return yaml_data

