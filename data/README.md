# Generative AI for Synthetic Data Creation

## Python Files

1. `chatgpt_coffee_data_gen.py` - data generator for coffee shop data, built using ChatGPT
2. `coffee_shop_data_gen_initial.py` - initial version of data generator for coffee shop data, built using Copilot
3. `coffee_shop_data_gen_final.py` - final version of data generator for coffee shop data
4. `coffee_shop_data_gen_tests.py` - unit tests for data generator for coffee shop data
5. `demographic_data_gen.py` - data generator for demographic data
6. `residential_address_data_gen.py` - data generator for residential address data

## Liniting and Testing Process

```bash
# files linted with flake8 (alternative to black)
python3 -m pip install -U flake8
python3 -m flake8 --ignore E501 *.py --benchmark -v 

# files tested with pytest
python3 -m pip install -U pytest pytest-benchmark pytest-cov pytest-black
python3 -m pytest coffee_shop_data_gen_tests.py -v
python3 -m coverage report coffee_shop_data_gen_final.py
```