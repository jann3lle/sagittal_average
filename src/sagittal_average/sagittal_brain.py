from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np
from pathlib import Path

data_dir = Path(__file__).resolve().parent / "data"
default_input = data_dir / "brain_sample.csv"
default_output = data_dir / "brain_average.csv"

def run_averages(file_input= default_input, file_output= default_output):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is the average for each sagittal/horizontal plane (rows)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    # averages = planes.mean(axis=0)[np.newaxis, :]
    averages = planes.mean(axis=1)

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')


if __name__ == "__main__":
    parser = ArgumentParser(description="Calculates the average for each sagittal-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default= default_input,
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default= default_output,
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)
