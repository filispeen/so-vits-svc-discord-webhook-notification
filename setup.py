from setuptools import find_packages, setup

setup(
    name='F_Discord_webhook',
    packages=find_packages(),
    version='2.0.9',
    description='Discord Webhook Messanger',
    author='FILISPEEN',
    install_requires=['discord', 'pytz', 'aiohttp', 'argparse', 'watchdog'],
)