"""Generate a series of plots focusing on the Kramer Ave slide, 8/18/2015."""

from pathlib import Path

import obspy
import matplotlib.pyplot as plt


data_dir = Path(__file__).parent / "data" / "kramer_08182015"
data_files = data_dir.glob("*.mseed")

output_dir = Path(__file__).parent / "output"

for file in data_files:
    output_file = "kramer_" + file.stem + ".png"
    output_path = output_dir / output_file

    print("Writing file:", output_path)

    stream = obspy.read(file)

    fig, axes = plt.subplots(nrows=len(stream), ncols=1, figsize=(24, len(stream) * 4), sharex=True)
    
    for ax, trace in zip(axes, stream):
        ax.plot(trace.times(), trace.data)
        ax.set_title(f'{trace.stats.station}.{trace.stats.channel}')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Amplitude')
        ax.set_ylim([-24_000, 16_000])

    plt.tight_layout()

    fig.savefig(output_path)

    # Pause to view a specific plot.
    # if "1hr" in output_file:
    #     plt.show()

    plt.close(fig)  # Close the plot to free up memory

    # Make a day plot as well, for 24-hr plots.
    if "24hr" in file.stem:
        for index, trace in enumerate(stream):
            # Only plot middle trace for now.
            if index != 1:
                continue
            output_file = f"kramer_dayplot_{file.stem}-{index}.png"
            output_path = output_dir / output_file

            print("  Writing dayplot:", output_path)
            trace.plot(type="dayplot", outfile=output_path, size=(2400, 1200))