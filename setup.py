from setuptools import find_packages, setup

setup(
    name='svc_ds_webhook',
    packages=find_packages(),
    version='2.0.19',
    description='Discord Webhook Messanger',
    license='MIT',
    author='FILISPEEN',
    install_requires=['discord', 'pytz', 'aiohttp', 'argparse', 'watchdog'],
    entry_points={
        "console_scripts": [
            "svc_ds_webhook = F_Discord_webhook.webhook:main"],},
    author = "FILISPEEN",
    url = 'https://github.com/filispeen/so-vits-svc-discord-webhook-notification',
    keywords = ['discord', 'webhook', 'discord_webhook', 'svc', 'so-vits-svc-fork', 'so-vits-svc-fork-discord-webhook'],
      classifiers=[
    'Development Status :: 5 - Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developer',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
