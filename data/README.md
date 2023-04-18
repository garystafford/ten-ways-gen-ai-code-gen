# Generative AI for Synthetic Data Creation

## Liniting and Testing Process

```bash
# files linted with flake8
python3 -m pip install -U flake8
python3 -m flake8 --ignore E501 *.py --benchmark -v 

# files tested with pytest
python3 -m pip install -U pytest pytest-benchmark pytest-cov pytest-black
python3 -m pytest coffee_shop_data_gen_tests.py -v
python3 -m coverage report coffee_shop_data_gen_final.py
```