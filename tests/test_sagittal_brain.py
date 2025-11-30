import numpy as np
import sys
from sagittal_average import run_averages
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
tests = Path(__file__).parent 

input = np.zeros((20, 20))
input[-1, :] = 1
np.savetxt("brain_sample.csv", input, fmt='%d', delimiter=',')

# The expected result is all zeros, except the last one, it should be 1
expected = np.zeros(20)
expected[-1] = 1

run_averages(file_input="brain_sample.csv",
             file_output="brain_average.csv")

result = np.loadtxt(tests / "brain_average.csv",  delimiter=',')
np.testing.assert_array_equal(result, expected)


