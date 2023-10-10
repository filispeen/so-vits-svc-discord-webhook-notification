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
parser.add_argument('--directory', default='./', help='Путь к директории, которую нужно мониторить')

args = parser.parse_args()

async def main(url, dataset_name, train_folder_name, train_start_date, percent, generation, training_time):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title=f"Процесс тренування АІ ({dataset_name}, {train_folder_name})", description=f"Дата запуска: {datetime.fromtimestamp(train_start_date)}")
        embed.add_field(name="Вивченних поколінь", value=generation, inline=True)
        total_training_time=datetime.fromtimestamp(datetime.timestamp(datetime.now())) - datetime.fromtimestamp(train_start_date)
        embed.add_field(name="Весь вичерпанний час", value=total_training_time, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Процент закінченого тренування", value=f"{percent}%", inline=True)
        embed.add_field(name="Примірний час закінчення", value=training_time, inline=True)
        await webhook.send(embed=embed, username="TEST WEBHOOK")

def calculate_epochs(training_time_seconds, epoch_duration_seconds):
    epochs = training_time_seconds / epoch_duration_seconds
    return int(epochs)

def on_file_created(event):
    if event.src_path.startswith(directory) and event.src_path.endswith('.txt'):
        filename = os.path.basename(event.src_path)
        if filename.startswith('G_'):
            epochs_to_train = args.epochs_to_train
            num = filename.replace("G_", "").replace(".txt", "")
            epochs_to_train-=float(num)
            percent = str((float(num) / float(epochs_to_train)) * 100)
            percent = percent[:4]
            current_speed = random.randint(9, 13)
            training_time_minutes = epochs_to_train / current_speed
            training_time_seconds = training_time_minutes * 60
            training_hours = int(training_time_minutes // 60)
            training_minutes = int(training_time_minutes % 60)
            training_seconds = int(training_time_seconds % 60)
            training_time=f"~{training_hours}год, {training_minutes}хв, {training_seconds}сек"
            loop = asyncio.new_event_loop()  # Создаем новый event loop
            asyncio.set_event_loop(loop)
            loop.run_until_complete(main(url, dataset_name, train_folder_name, train_start_date, percent, generation=f"{num}, потрібно {int(args.epochs_to_train)} осталось {int(args.epochs_to_train)-int(num)}", training_time=training_time))
            loop.close()

url = args.url
#url = "https://discord.com/api/webhooks/1159946968945152101/Z-Ad6BO0tWkIPGn6hibsKAehzLJ6tsyk1aOjDwuorG9krGFBXRZdPBhNhG9uVxpf2_y-"
train_start_date = datetime.timestamp(datetime.now(pytz.timezone('Europe/Kiev')))
dataset_name = args.dataset_name
train_folder_name = args.train_folder_name
train_directory = args.directory
directory = train_directory
#dataset_name = "SexMan"
#train_folder_name = "Train"

# Создаем директорию, если она не существует
if not os.path.exists(directory):
    os.makedirs(directory)

# Настройка мониторинга за директорией
event_handler = FileSystemEventHandler()
event_handler.on_created = on_file_created
observer = Observer()
observer.schedule(event_handler, path=directory, recursive=False)
observer.start()

if __name__ == '__main__':
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
