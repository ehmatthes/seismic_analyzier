from pathlib import Path

import pandas as pd

data_root = Path(__file__).parent / "data"
data_dir = "fdsnws-dataselect_2024-05-01t05_33_49z"
data_file = "AT.SIT..BHZ.M.2014-09-18T180000.000000.csv"

path = data_root / data_dir / data_file

df = pd.read_csv(path, skiprows=18)


# Plot data.
import plotly.express as px

# Only plot every _th point.
plot_df = df.iloc[::100]
fig = px.line(plot_df, x="Time", y=" Sample")

fig.update_traces(marker=dict(size=0.1), line=dict(width=0.1))

fig.show()




# import pdb
# breakpoint()
