# Vexor World - MultiBot

## Introduction
Vexor World - MultiBot is a Discord bot written in Python using the Discord.py library. It monitors game servers and updates its Discord status based on the number of players online using data fetched from the BattleMetrics API. This bot is designed to run multiple instances, each monitoring a different server.

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/vexor-world-multibot.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Update the `BOT_TOKENS` and `SERVER_IDS` variables in `status.py` with your bot tokens and server IDs.

## Discord Bot Setup
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).

2. Click on **New Application** and give your application a name.

3. Navigate to the **Bot** tab on the left sidebar.

4. Click on **Add Bot** and confirm.

5. Copy the bot token by clicking on **Copy** under the bot username.

6. Update the `BOT_TOKENS` variable in `status.py` with the copied token.

7. Navigate to the **OAuth2** tab on the left sidebar.

8. Under **OAuth2 URL Generator**, select the **bot** scope.

9. Select the required permissions for your bot (e.g., Read Messages, Send Messages, etc.).

10. Copy the generated URL and paste it into your browser. Follow the instructions to add the bot to your Discord server.

## Usage
1. Ensure that you have Python installed on your system (version 3.7 or higher recommended).

2. Navigate to the directory where you cloned the repository.

3. Run the bot by executing the following command:

    ```bash
    python status.py
    ```

4. The bot will start running and update its status based on the number of players online in the specified game servers.

## Contributing
If you'd like to contribute to this project, you can:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them to your branch.
- Push your changes to your fork.
- Submit a pull request to the main repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
