import strgen, ctypes, os


class Discord:
    def __init__(self):
        self.regularExpression = "[N]([a-zA-Z0-9]{23})\.([a-zA-Z0-9]{6})\.([a-zA-Z0-9]{27})" # This is the regular expression for discord.
        self.generated = 0


    def generate(self, amount):
        for _ in range(amount):
            discordToken = strgen.StringGenerator(self.regularExpression).render()
            discordToken = discordToken.replace("..", ".")
            print(discordToken)
            self.generated += 1
            self.write(discordToken)
            self.title()
    
    def write(self, discordToken):
        if os.path.isfile("./tokens.txt"):
            writeToken = open("./tokens.txt", "a")
            writeToken.write(f"{discordToken}\n")
        else:
            open("./tokens.txt", "w").close() # Simply create the file.

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"[Discord Token Generator] Developer Sympthey#9308 | Generated: {self.generated}")


if __name__ == "__main__":
    open("./tokens.txt", "w").close() # Create and clear our token file each time
    token = Discord()
    amountToGen = int(input("Enter amount of tokens to generate: "))
    token.generate(amountToGen)
