"""Generate a series of plots focusing on the Kramer Ave slide, 8/18/2015."""

from pathlib import Path

import obspy


data_dir = Path(__file__).parent / "data" / "kramer_08182015"
data_files = data_dir.glob("*.mseed")

output_dir = Path(__file__).parent / "output"

for file in data_files:
    output_file = "kramer_" + file.name.removesuffix(".mseed") + ".png"
    output_path = output_dir / output_file
    print("Writing file:", output_path)

    stream = obspy.read(file)
    stream.plot(outfile=output_path)

    # Pause and view a specific plot:
    if "2hr" in file.name:
        stream.plot()