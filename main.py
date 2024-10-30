from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:insert your oauth token', client_id='insert your client_id', nick='insert your twitch account nickname', prefix='!',
                         initial_channels=['Put here your channels to gather from'])

    async def event_message(self, message):
        print(message.content, "|", message.channel.name)
        with open("chat.txt", "a", encoding = "utf-8") as file:
            file.write(message.content + "\n")
        await self.handle_commands(message)

bot = Bot()
bot.run()
