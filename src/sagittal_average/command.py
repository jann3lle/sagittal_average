from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib import Path
from .sagittal_brain import run_averages

data_dir = Path(__file__).resolve().parent / "data"
default_input = data_dir / "brain_sample.csv"
default_output = data_dir / "brain_average.csv"

def main():
    parser = ArgumentParser(description="Calculates the average for each sagittal-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default= default_input,
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default= default_output,
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)

