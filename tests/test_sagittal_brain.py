import numpy as np
from pathlib import Path
from sagittal_average.sagittal_brain import run_averages
import tempfile


def test_run_averages():
    # Use a temporary directory so tests don't pollute your repo
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Create the input dataset
        data_input = np.zeros((20, 20))
        data_input[-1, :] = 1

        input_file = tmpdir / "brain_sample.csv"
        output_file = tmpdir / "brain_average.csv"

        # Save the input file
        np.savetxt(input_file, data_input, fmt="%d", delimiter=",")

        # Expected: all zeros except last position = 1
        expected = np.zeros(20)
        expected[-1] = 1

        # Run your function
        run_averages(file_input=input_file, file_output=output_file)

        # Load the output
        result = np.loadtxt(output_file, delimiter=",")

        # Compare
        np.testing.assert_array_equal(result, expected)
