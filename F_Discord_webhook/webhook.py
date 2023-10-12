from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from datetime import datetime
from discord import Webhook
import argparse
import asyncio
import aiohttp
import discord
import random
import time
import pytz
import os

parser = argparse.ArgumentParser(description="DS WebHook")

parser.add_argument("--url", dest="url", required=True, type=str)
parser.add_argument("--dataset_name", dest="dataset_name", default="AI", type=str)
parser.add_argument("--train_folder_name", dest="train_folder_name", default=".", type=str)
parser.add_argument("--epochs_to_train", dest="epochs_to_train", required=True, type=float)
parser.add_argument('--directory', default='./', help='Path to the directory to monitor')

args = parser.parse_args()

async def process(url, dataset_name, train_folder_name, train_start_date, percent, generation, training_time):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        if int(percent) >= 99:
            embed = discord.Embed(title=f"AI Training Process ({dataset_name}, {train_folder_name}) completed.", description=f"Start Date: {datetime.fromtimestamp(train_start_date)}")
        else:
            embed = discord.Embed(title=f"AI Training Process ({dataset_name}, {train_folder_name})", description=f"Start Date: {datetime.fromtimestamp(train_start_date)}")
        embed.add_field(name="Generations Trained", value=generation, inline=True)
        total_training_time = datetime.fromtimestamp(datetime.timestamp(datetime.now())) - datetime.fromtimestamp(train_start_date)
        embed.add_field(name="Total Elapsed Time", value=total_training_time, inline=True)
        if not int(percent) >= 99:
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="Percentage of Training Completed", value=f"{percent}%", inline=True)
            embed.add_field(name="Estimated Completion Time", value=training_time, inline=True)
        await webhook.send(embed=embed, username="TEST WEBHOOK")

def calculate_epochs(training_time_seconds, epoch_duration_seconds):
    epochs = training_time_seconds / epoch_duration_seconds
    return int(epochs)

def on_file_created(event):
    if event.src_path.startswith(directory) and event.src_path.endswith('.pth'):
        filename = os.path.basename(event.src_path)
        if filename.startswith('G_'):
            print(filename)
            epochs_to_train = args.epochs_to_train
            num = filename.replace("G_", "").replace(".pth", "")
            epochs_to_train -= float(num)
            percent = (float(num) / float(epochs_to_train)) * 100
            percent = str(round(percent))
            if int(percent) >= 100:
                percent = "100"
            try:
                percent = percent[:4]
            except ZeroDivisionError:
                percent = "100"
            if args.epochs_to_train == num:
                percent = "100"
            current_speed = random.randint(9, 13)
            training_time_minutes = epochs_to_train / current_speed
            training_time_seconds = training_time_minutes * 60
            training_hours = int(training_time_minutes // 60)
            training_minutes = int(training_time_minutes % 60)
            training_seconds = int(training_time_seconds % 60)
            training_time = f"~{training_hours} hours, {training_minutes} minutes, {training_seconds} seconds"
            loop = asyncio.new_event_loop()  # Create a new event loop
            asyncio.set_event_loop(loop)
            loop.run_until_complete(process(url, dataset_name, train_folder_name, train_start_date, percent, generation=f"{num}, {int(args.epochs_to_train) - int(num)} remaining", training_time=training_time))
            loop.close()
            if int(percent) >= 99:
                exit()

url = args.url
train_start_date = datetime.timestamp(datetime.now(pytz.timezone('Europe/Kiev')))
dataset_name = args.dataset_name
train_folder_name = args.train_folder_name
train_directory = args.directory
directory = train_directory

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    raise FileNotFoundError(f"Folder not found: {directory}")

# Set up directory monitoring
event_handler = FileSystemEventHandler()
event_handler.on_created = on_file_created
observer = Observer()
observer.schedule(event_handler, path=directory, recursive=False)
observer.start()

def main():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
