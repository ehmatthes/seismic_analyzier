from pathlib import Path

import obspy


data_root = Path(__file__).parent / "data"

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