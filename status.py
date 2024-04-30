import discord
import aiohttp
import asyncio
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define bot tokens and server IDs
BOT_TOKENS = ['BOT_TOKEN_1', 'BOT_TOKEN_2']  # Add more bot tokens as needed
SERVER_IDS = ['SERVER_ID_1', 'SERVER_ID_2']  # Add more server IDs as needed

class MultiBot(discord.Client):
    def __init__(self, bot_tokens, server_ids):
        super().__init__()
        self.bot_tokens = bot_tokens
        self.server_ids = server_ids
        self.keep_running = True

    async def on_ready(self):
        print(Fore.GREEN + 'Vexor World - Players Counter is online!' + Style.RESET_ALL)

        # Start an update status task for each bot
        for bot_token, server_id in zip(self.bot_tokens, self.server_ids):
            print(Fore.YELLOW + f'Starting update status task for bot with token {bot_token}' + Style.RESET_ALL)
            self.loop.create_task(self.update_status(bot_token, server_id))

    async def update_status(self, bot_token, server_id):
        try:
            while self.keep_running:
                print(Fore.CYAN + f'Fetching data from BattleMetrics API for server {server_id}' + Style.RESET_ALL)
                async with aiohttp.ClientSession() as session:
                    # Fetch data from BattleMetrics API
                    url = f'https://api.battlemetrics.com/servers/{server_id}'
                    async with session.get(url) as response:
                        if response.status == 200:
                            server_data = await response.json()
                            players_count = server_data['data']['attributes']['players']
                            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{players_count} players online'))
                            print(Fore.GREEN + f'Successfully updated status for bot with token {bot_token}: {players_count} players online' + Style.RESET_ALL)
                            print(Fore.GREEN + 'Status updated.' + Style.RESET_ALL)
                        else:
                            print(Fore.RED + f'Failed to fetch data from BattleMetrics API for server {server_id}' + Style.RESET_ALL)
                await asyncio.sleep(25)  # Update status every 25 seconds
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

    async def on_shutdown(self):
        print(Fore.YELLOW + "Shutting down..." + Style.RESET_ALL)
        self.keep_running = False
        await self.logout()

async def main():
    multi_bots = [MultiBot([token], [server_id]) for token, server_id in zip(BOT_TOKENS, SERVER_IDS)]
    print(Fore.YELLOW + 'Starting multi-bot instances...' + Style.RESET_ALL)
    tasks = [bot.start(token) for bot, token in zip(multi_bots, BOT_TOKENS)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Received KeyboardInterrupt, shutting down..." + Style.RESET_ALL)
        for task in asyncio.all_tasks():
            task.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.stop()
