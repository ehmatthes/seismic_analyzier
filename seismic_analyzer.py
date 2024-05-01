from pathlib import Path

import pandas as pd

data_root = Path(__file__).parent / "data"

# Starrigavan slide, 9/2014
# data_dir = "fdsnws-dataselect_2024-05-01t05_33_49z"
# data_file = "AT.SIT..BHZ.M.2014-09-18T180000.000000.csv"

# S Kramer slide, 8/2015
data_dir = "fdsnws-dataselect_2024-05-01t22_02_42z"
# data_file = "AT.SIT..BHE.M.2015-08-18T000000.000000.csv"
# data_file = "AT.SIT..BHN.M.2015-08-18T000000.000000.csv"
data_file = "AT.SIT..BHZ.M.2015-08-18T000000.000000.csv"


path = data_root / data_dir / data_file

# df = pd.read_csv(path, skiprows=18)


# # Plot data.
# import plotly.express as px

# # Only plot every _th point.
# plot_df = df.iloc[::10]
# fig = px.line(plot_df, x="Time", y=" Sample")

# fig.update_traces(marker=dict(size=0.1), line=dict(width=0.1))

# fig.show()




# import pdb
# breakpoint()



import obspy

# Kramer mseed data.
path = data_root / "fdsnws-dataselect_2024-05-01t22_27_09z-southkramer.mseed"

# Starrigavan mseed data.
path = data_root / "fdsnws-dataselect_2024-05-01t22_38_36z-starrigavan.mseed"

# Sand Dollar mseed data.
path = data_root / "fdsnws-dataselect_2024-05-01t22_49_03z-sanddollar.mseed"

# Random dry day, no event (4/30/24).
path = data_root / "fdsnws-dataselect_2024-05-01t22_52_52z-043024_no_event.mseed"


stream = obspy.read(path)

stream.plot()