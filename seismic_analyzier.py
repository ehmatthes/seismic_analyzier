from pathlib import Path

import pandas as pd

data_root = Path(__file__).parent / "data"
data_dir = "fdsnws-dataselect_2024-05-01t05_33_49z"
data_file = "AT.SIT..BHZ.M.2014-09-18T180000.000000.csv"

path = data_root / data_dir / data_file

df = pd.read_csv(path, skiprows=18)

import pdb
breakpoint()
