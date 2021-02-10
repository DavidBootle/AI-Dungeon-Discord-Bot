from webscraper import Game
import discord
import os

client = discord.Client()

games = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'ai-dungeon':

      if message.content.startswith('/newgame'): #NEWGAME
          await message.channel.send('Starting new game...\nThis may take up to 30 seconds...')
          games[message.guild.id] = Game()
          options = games[message.guild.id].get_starting_options()
          sendstring = 'Type the number of the option you want to choose:\n'
          for option in options:
            sendstring += str(option['number']) + ': ' + str(option['text']) + '\n'
          sendstring = sendstring[:-1] # remove \n at the end
          await message.channel.send(sendstring)
      
      
      elif client.cached_messages[len(client.cached_messages)-1].content.startswith('/newgame'): # RESPONSE TO SETTING PROMPT FOR NEWGAME
        response = message.content
        print(response)

      if message.content.startswith('/endgame'): #ENDGAME
        await message.channel.send('Ending game...')
        if(games[message.guild.id].end_game()):
          del games[message.guild.id]
          await message.channel.send('Game ended')

client.run(os.getenv('TOKEN'))