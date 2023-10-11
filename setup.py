from setuptools import find_packages, setup

setup(
    name='F_Discord_webhook',
    packages=find_packages(),
    version='2.0.19',
    description='Discord Webhook Messanger',
    author='FILISPEEN',
    install_requires=['discord', 'pytz', 'aiohttp', 'argparse', 'watchdog'],
    entry_points={
        "console_scripts": [
            "svc_ds_webhook = F_Discord_webhook.webhook:main"],},
)
