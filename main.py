import discord
from discord.ext import commands
from config import settings
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Только Sora"))
        await asyncio.sleep(10)
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "YouTube"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="помощь: .help"))
        await asyncio.sleep(10)

@bot.command() 
async def rank(ctx): 
    author = ctx.message.author 
    await ctx.message.delete()
    await ctx.send(f'{author.mention}, !rank? не, не слышал') 

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg) 

@bot.command()
@commands.has_permissions(administrator=True)
async def sayemb(ctx, name, *, arg=None):
		if name == 'Жирный':
			await ctx.message.delete()
			embed = discord.Embed(color = 0x80, title = arg, description="")
			await ctx.send(embed = embed)
		elif name == 'Тонкий':
			await ctx.message.delete()
			embed = discord.Embed(color = 0x80, title = "", description=arg)
			await ctx.send(embed = embed)
		else:
			await ctx.send(embed=discord.Embed(color=0x80, title="У-упс...", description="Выберите шрифт."))

@bot.command()
async def vote(ctx, *, arg=None):
	if arg==None:
		embed = discord.Embed(color = 0x80, title = 'У-упс...', description='Для голосования должен быть хотя бы введён один символ.')
		await ctx.send(embed=embed)
	else:
		author = ctx.message.author
		await ctx.message.delete()
		emb = discord.Embed(title=f'{author.name} Начинает голосование!', description=f'{arg}', color=0x80)
		message = await ctx.send(embed=emb)
		await message.add_reaction('✅')
		await message.add_reaction('❌')			    

@bot.command()
async def sad(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x80, description = f'{author.mention} грустит ')
    embed.set_image(url = "https://media.discordapp.net/attachments/817140764999548928/817328931962355712/sad_3.gif")
    await ctx.message.delete()
    await ctx.send(embed = embed)

@bot.command()
async def kiss(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(color = 0x80, description = f'{author.mention} поцеловал {member.mention}')
    embed.set_image(url = "https://i.gifer.com/QPB7.gif")
    await ctx.message.delete()
    await ctx.send(embed = embed)

@bot.command()
async def pat(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(color = 0x80, description = f'{author.mention} погладил {member.mention}')
    embed.set_image(url = "https://psv4.userapi.com/c532036/u467520766/docs/d18/3b4e2c9704ac/1530443619_2.gif?extra=DI9v74Me7Cc8jtztfRmVOQRHw1ogjYrF_Arim-tfQbujoEWwAS78Zb41o4cjsf29nFfJHf0mdW7V_hgIbdft1ISa7esjyISOnTzolU1eOtCKa9L0lpZXcUCRdbSDdRGVBkUAGaOq1jkLmILwkwzcIkA")
    await ctx.message.delete()
    await ctx.send(embed = embed)

@bot.command()
async def kill(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(color = 0x80, description = f'{author.mention} убил {member.mention}')
    embed.set_image(url = "https://i.gifer.com/7jkI.gif")
    await ctx.message.delete()
    await ctx.send(embed = embed)

@bot.command()
async def hug(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(color = 0x80, description = f'{author.mention} обнимает {member.mention}')
    embed.set_image(url = "https://i.gifer.com/B7bp.gif")
    await ctx.message.delete()
    await ctx.send(embed = embed)

bot.run(settings['token']) 
