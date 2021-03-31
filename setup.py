import setuptools


setuptools.setup(
    name='bulq-input-exchange-rates-api',
    version='0.0.1',
    install_requires=[],
    packages=setuptools.find_packages(),
    entry_points={
        'bulq.plugins.input': [
            f'exchange_rates_api = bulq_input_exchange_rates_api',
        ],
    }
)

