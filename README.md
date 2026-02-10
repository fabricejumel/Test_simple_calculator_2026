# Test_simple_calculator_2026

Mode developpeur 
#installation
git clone httos://github.com:fabricejumel/Test_simple_calculator_2026.git

cd Test_simple_calculator_2026
python -m venv .venv
source .venv/bin/activate
pip install -e .[test]

python -m pytest -vv --cov --cov-branch --cov-report=term-missing  --durations=0
============================================================================================================ test session starts ============================================================================================================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0 -- /home/astro/wp_admco_2026/Test_simple_calculator_2026/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/astro/wp_admco_2026/Test_simple_calculator_2026
configfile: pyproject.toml
testpaths: tests
plugins: cov-7.0.0
collected 26 items

tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_float PASSED                                                                                                                                               [  3%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_string PASSED                                                                                                                                              [  7%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_by_one PASSED                                                                                                                                                [ 11%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_negative PASSED                                                                                                                                              [ 15%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_positive PASSED                                                                                                                                              [ 19%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_result_float PASSED                                                                                                                                          [ 23%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_denominator PASSED                                                                                                                                            [ 26%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_numerator PASSED                                                                                                                                              [ 30%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_bool PASSED                                                                                                                                                  [ 34%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_float PASSED                                                                                                                                                 [ 38%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_none PASSED                                                                                                                                                  [ 42%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_string PASSED                                                                                                                                                [ 46%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_negative PASSED                                                                                                                                                [ 50%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_positive PASSED                                                                                                                                                [ 53%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_zero PASSED                                                                                                                                                    [ 57%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_large_numbers PASSED                                                                                                                                                      [ 61%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_invalid_types PASSED                                                                                                                                             [ 65%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_negative PASSED                                                                                                                                            [ 69%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_one PASSED                                                                                                                                                 [ 73%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_positive PASSED                                                                                                                                            [ 76%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_zero PASSED                                                                                                                                                [ 80%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_invalid_types PASSED                                                                                                                                            [ 84%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_negative PASSED                                                                                                                                           [ 88%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_positive PASSED                                                                                                                                           [ 92%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_zero PASSED                                                                                                                                               [ 96%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_type_consistency PASSED                                                                                                                                                   [100%]

============================================================================================================== tests coverage ===============================================================================================================
______________________________________________________________________________________________ coverage: platform linux, python 3.12.3-final-0 ______________________________________________________________________________________________

Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
src/calculator/__init__.py                3      0      0      0   100%
src/calculator/simple_calculator.py      19      0     10      0   100%
tests/test_simple_calculator.py         123      1      2      1    98%   198
---------------------------------------------------------------------------------
TOTAL                                   145      1     12      1    99%
============================================================================================================= slowest durations =============================================================================================================
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_float
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_float
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_none
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_one
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_string
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_bool
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_negative
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_result_float
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_large_numbers
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_negative
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_denominator
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_by_one
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_invalid_types
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_float
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_float
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_negative
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_invalid_types
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_string
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_zero
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_string
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_type_consistency
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_numerator
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_zero
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_none
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_string
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_type_consistency
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_type_consistency
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_result_float
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_invalid_types
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_negative
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_positive
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_numerator
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_positive
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_denominator
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_by_one
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_string
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_zero
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_negative
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_float
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_one
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_positive
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_invalid_types
0.00s setup    tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_string
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_positive
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_zero
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_zero
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_large_numbers
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_float
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_zero
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_invalid_types
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_bool
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_negative
0.00s call     tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_by_one
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_bool
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_positive
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_numerator
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_none
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_large_numbers
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_one
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_positive
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_negative
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_denominator
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_positive
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_result_float
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_zero
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_zero
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_zero
0.00s teardown tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_invalid_types
============================================================================================================ 26 passed in 0.11s =============================================================================================================


