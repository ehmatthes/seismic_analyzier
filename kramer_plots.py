"""Generate a series of plots focusing on the Kramer Ave slide, 8/18/2015."""

from pathlib import Path

import obspy
import matplotlib.pyplot as plt


data_dir = Path(__file__).parent / "data" / "kramer_08182015"
data_files = data_dir.glob("*.mseed")

output_dir = Path(__file__).parent / "output"

# for file in data_files:
#     output_file = "kramer_" + file.name.removesuffix(".mseed") + ".png"
#     output_path = output_dir / output_file
#     print("Writing file:", output_path)

#     stream = obspy.read(file)
#     # stream.plot(outfile=output_path)
#     # fig = stream.plot(handle=True)

#     # ax = fig.axes[0]
#     # ax.set_ylim([-24_000, 16_000])
#     # fig.savefig(output_path)

#     # Manually generate plot.
#     data = stream[0].data
#     times = stream[0].times()

#     # Create the plot
#     fig, ax = plt.subplots()
#     ax.plot(times, data, color='red')
#     ax.set_ylim([-24000, 16000])

#     # Additional formatting
#     ax.set_title('Seismic Data')
#     ax.set_xlabel('Time (s)')
#     ax.set_ylabel('Amplitude')

#     # Save the plot
#     fig.savefig(output_path)
#     plt.close(fig)


for file in data_files:
    output_file = "kramer_" + file.stem + ".png"
    output_path = output_dir / output_file

    print("Writing file:", output_path)

    # Read the seismic data
    stream = obspy.read(file)

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=len(stream), ncols=1, figsize=(24, len(stream) * 4), sharex=True)
    
    # Check if we have only one trace to avoid indexing errors
    if len(stream) == 1:
        axes = [axes]  # Make it iterable

    # Plot each trace in a separate subplot
    for ax, trace in zip(axes, stream):
        ax.plot(trace.times(), trace.data)
        ax.set_title(f'{trace.stats.station}.{trace.stats.channel}')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Amplitude')
        ax.set_ylim([-24_000, 16_000])

        # Set specific y-axis limits if necessary
        # ax.set_ylim([-24000, 16000])

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot
    fig.savefig(output_path)
    plt.close(fig)  # Close the plot to free up memory


    break