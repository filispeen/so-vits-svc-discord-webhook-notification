from setuptools import find_packages, setup

setup(
    name='svc_ds_webhook',
    packages=find_packages(),
    version='2.0.22',
    description='Discord Webhook Messanger',
    license='MIT',
    author='FILISPEEN',
    long_description = """
This is a Python script designed to monitor a specified directory for the progress of an AI training process and send real-time updates to a Discord webhook. It is a versatile tool suitable for tracking and reporting on the status of AI training runs.

The script uses the Watchdog library to monitor the specified directory for file creation events. When a new file with a ".pth" extension is created, the script processes it to extract information about the AI training progress.

Key features and functionality include:
- Real-time updates: The script reports training progress to a Discord webhook, including details such as generations trained, the percentage of training completed, and estimated time for completion.
- Customizable parameters: You can specify the Discord webhook URL, dataset name, and other options through command-line arguments.
- Support for different time zones: The script uses the Pytz library to handle time zones, ensuring accurate timestamps in notifications.

To use this script, simply set up the necessary parameters, run it, and it will continuously monitor the specified directory for training progress updates. It's a handy tool for keeping track of AI training processes and staying informed about their status.

For detailed usage instructions, please refer to the documentation or the project's README file.
""",
    install_requires=['discord', 'pytz', 'aiohttp', 'argparse', 'watchdog'],
    entry_points={
        "console_scripts": [
            "svc_ds_webhook = F_Discord_webhook.webhook:main"],},
    url = 'https://github.com/filispeen/so-vits-svc-discord-webhook-notification',
    keywords = ['discord', 'webhook', 'discord_webhook', 'svc', 'so-vits-svc-fork', 'so-vits-svc-fork-discord-webhook'],
      classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
