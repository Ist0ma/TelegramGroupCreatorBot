from pyrogram import Client, filters

class MyBot:
    def __init__(self):
        self.account = Client("my_account")
        self.app = Client('my_bot')

    def create_group(self, user_id, group_name):
        with self.account:
            self.account.create_group(group_name, user_id)

    def start(self):
        @self.app.on_message(filters.command('start'))
        def start(client, message):
            user_id = message.from_user.id
            group_name = f"Group for {message.from_user.first_name}"
            self.create_group(user_id, group_name)

        self.app.run()

if __name__ == '__main__':
    bot = MyBot()
    bot.start()
