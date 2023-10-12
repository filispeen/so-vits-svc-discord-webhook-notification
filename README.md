[![Upload Python Package](https://github.com/filispeen/so-vits-svc-discord-webhook-notification/actions/workflows/python_publish.yml/badge.svg)](https://github.com/filispeen/so-vits-svc-discord-webhook-notification/actions/workflows/python_publish.yml)
<h1 id="how-to-use-the-svc-ai-training-progress-monitoring-script">How to Use the SVC AI Training Progress Monitoring Script</h1>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before using the script, ensure you have the following prerequisites in place:</p>
<ol>
<li><p><strong>Python</strong>: Make sure you have Python installed on your system. You can download it from <a href="https://www.python.org/downloads">python.org</a>.</p>
</li>
<li><p><strong>Git</strong>: You&#39;ll also need Git installed on your system to run the following command. You can download it from <a href="https://git-scm.com/downloads">git-scm.com</a>.</p>
</li>
<li><p><strong>Required Libraries</strong>: Install the required Python libraries, including the script&#39;s custom library, using the following commands:</p>
<pre><code class="language-bash">pip install watchdog aiohttp discord.py pytz
</code></pre>
</li>
<li><p><strong>PyPi package installation</strong>:</p>
<pre><code class="language-bash">pip install svc-ds-webhook
</code></pre>
</li>
</ol>
<h2 id="getting-started">Getting Started</h2>
<ol>
<li><p>Download the script to your local machine.</p>
</li>
<li><p>Open a terminal or command prompt and navigate to the directory where you&#39;ve saved the script.</p>
</li>
<li><p>Run the script using the following command:</p>
<pre><code class="language-bash">svc_ds_webhook --url <strong>YOUR_DISCORD_WEBHOOK_URL</strong> --dataset_name <strong>YOUR_DATASET_NAME</strong> --train_folder_name <strong>YOUR_TRAIN_FOLDER_NAME</strong> --epochs_to_train <strong>NUMBER_OF_EPOCHS</strong> --directory <strong>DIRECTORY_TO_MONITOR</strong>
</code></pre>
</li>
</ol>
<ul>
<li>Replace <strong>YOUR_DISCORD_WEBHOOK_URL</strong> with the actual Discord webhook URL where you want to receive updates.</li>
<li>Specify the <strong>YOUR_DATASET_NAME</strong> and <strong>YOUR_TRAIN_FOLDER_NAME</strong></li>
<li>Set <strong>NUMBER_OF_EPOCHS</strong> to the total number of epochs you want to train.</li>
<li>Specify the <strong>DIRECTORY_TO_MONITOR</strong>, which is the directory where you want the script to monitor for AI training progress updates.</li>
</ul>
<h2 id="script-execution">Script Execution</h2>
<p>Once the script is running, it will monitor the specified directory for changes in the training process. When new model files (with names starting with &#39;G_&#39;) are created in the directory, the script will send updates to the Discord webhook. It will provide information on the percentage of training completed and the estimated completion time.</p>
<p>The script will continue to run until you manually stop it using <code>Ctrl+C</code> in the terminal.</p>
<p>That&#39;s it! You now know how to use the AI training progress monitoring script to keep track of your AI model&#39;s training progress using a Discord webhook.</p>
