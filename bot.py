import discord
import os


client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('*hello'):
      await message.channel.send('Hello!')

    if message.content.startswith('*thanos'):
      await message.channel.send('Yeah he is a very good memer :kissing_heart:')

    if message.content.startswith('*creator'):
      await message.channel.send('Rintaro Shindo')

    if message.content.startswith('*Who Are You'):
      await message.channel.send('Konnichiwa I an Mai San :smile:')

    if message.content.startswith('*phoenixparavai'):
      await message.channel.send(':middle_finger:')

    if message.content.startswith('*botlink'):
      await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=870516676515479562&permissions=0&scope=bot')

    if message.content.startswith('*hwpdiscord'):
      await message.channel.send('https://discord.gg/W6yFtNaJ7D')
    
    if message.content.startswith('*kalacharam'):
      await message.channel.send('https://tenor.com/view/duppata-podunga-doli-duppata-mikasa-kalacharam-eren-teager-gif-24562150')

    if message.content.startswith('*chopper'):
      await message.channel.send('https://c.tenor.com/FdlVDT24lawAAAAd/one-piece-chopper-one-piece.gif')

    if message.content.startswith('*deku'):
      await message.channel.send('https://c.tenor.com/AqBvK0OMMcsAAAAC/dequu.gif')

    if message.content.startswith('*gojo'):
      await message.channel.send('https://c.tenor.com/CiJuhjUFaeIAAAAC/gojo-satoru-jujutsu-kaisen.gif')

    elif message.content.startswith('*what is the version'):
      await message.channel.send('2.0')

    elif message.content.startswith('*eren'):
      await message.channel.send('https://tenor.com/view/eren-eren-season4-season4eren-aot-eren-eren-eye-roll-gif-19744009')

    elif message.content.startswith('*i luv u'):
     await message.channel.send('https://s10.gifyu.com/images/SodaPDF-converted-Veida-ngotha.gif')

    elif message.content.startswith('*monke mon'):
      await message.channel.send('https://s10.gifyu.com/images/SodaPDF-converted-monke.gif')

    elif message.content.startswith('*paalkovaa page admin yaaru'):
     await message.channel.send('Dark 420 akka')

    elif message.content.startswith('*Who is ur boyfriend'):
      await message.channel.send('Frozenskull')

    elif message.content.startswith('*emily'):
      await message.channel.send(':new_moon_with_face:')

    elif message.content.startswith('*mai san kyoot'):
       await message.channel.send('https://c.tenor.com/8aL9mORrsBIAAAAd/bgs.gif')

    if message.content.startswith('*botdevinfo'):
        embedVar = discord.Embed(title="Hi I am Rintaro Shindo", description="I am a noob web dev and noob bot dev.I know HTML,CSS and few things in Javascript,Python and C++." , color=0x00ff00)
        embedVar.add_field(name="Instagram", value="https://www.instagram.com/saltedpoop57.exe/", inline=False)
        embedVar.add_field(name="Podcast", value="https://open.spotify.com/show/2j1zkHO8SktTVSPR1KNBSq", inline=False)
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('*cmds'):
        embedVar = discord.Embed(title="Bot Commands",color=0x00ff00)
        embedVar.add_field(name="Anime", value="*eren , *gojo , *deku , *chopper ", inline=False)
        embedVar.add_field(name="And some random shit nvm", value="*thanos , *phoenixparavai , *emily , *i luv u , *monke mon ", inline=False)
        await message.channel.send(embed=embedVar)

    
    
    
    



    


    
client.run("ODcwNTE2Njc2NTE1NDc5NTYy.YQN51Q.AEcdrwP92sX9I1wTRru3L9XdtSE")
