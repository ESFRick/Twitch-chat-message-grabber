from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:dopc45xngyq1a0nerpgl5jtsuhwk3p', client_id='i9kv0o5u4mcvjld64wcymu3oxx63hu', nick='not_esfr', prefix='!',
                         initial_channels=['JoinTheSystemm']) #Put here your channels to gather from

    async def event_message(self, message):
        print(message.content, "|", message.channel.name)
        with open("chat.txt", "a", encoding = "utf-8") as file:
            file.write(message.content + "\n")
        await self.handle_commands(message)

bot = Bot()
bot.run()
