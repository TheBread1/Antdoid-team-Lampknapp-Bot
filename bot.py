# imports
import json
from subprocess import PIPE
from discord import abc, member
from discord import voice_client
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext.commands.bot import Bot
from discord.ext.commands.converter import VoiceChannelConverter
from discord.guild import BanEntry
from discord.player import AudioPlayer, AudioSource, FFmpegAudio, FFmpegPCMAudio
import discord
import os
from discord import Member, Embed
from discord.ext import commands
from discord import Guild
from aiohttp import ClientSession
import aiohttp
from random import Random, randint, randrange
import random
from async_timeout import timeout
import asyncio
from discord.member import Member
from discord.voice_client import VoiceClient
import functools
import itertools
import math
from discord.utils import find
###########
#Notes    #
###########





######################################################################
#Customization :D
######################################################################
success_color = 0x1ffff1
fail_color = 0xff1f5b
musictimeout = 80
ownerdiscord = 'Bread.#7518' # Unless you know what to do if something breaks, I'd keep this in
prefix = '~' #Change the prefix to literally anything you want, or just keep it as this default
token = "Replace this with your bot's token."








######################################################################
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
client = discord.Client()
print('Starting...')
# account information printer
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f'Prefix is {prefix}, oh also only Bread. is behind this bot, nobody else!'))
    try:
        print(' ####    ####\n##############\n##############\n ############\n   ########\n     ####\n--------------') #Just some art for startup :)
        print(f'{bot.user.name} | {bot.user.id}')
        print(f'token: {token}')
    except Exception as p:
        print(p)









# message viewey bit (I really don't know why it won't run without this...)
@client.event
async def on_message(message):
    mc = (message.content)
    m = (message)
    print(mc)









#message responder
@bot.command(name='hello')
async def _deeznuts(ctx):

    greetings = open(file='greetings.txt', mode='r').readlines()
    pp = randrange(1,int(len(greetings)))
    await ctx.send(f'{(greetings[pp])}{ctx.author.mention}')



@bot.command(name='howmanyservers')
async def servers(ctx):
    servers = len(bot.guilds)
    await ctx.send(f"I'm in {servers} servers")

@bot.command(name='devhelp')
async def _contactdev(ctx):
    embed=discord.Embed(title=f"Here's the dev's discord!", description=f"`{ownerdiscord}`", color=success_color)
    await ctx.send(embed=embed)






@bot.command(name='say4me')
async def _sayforme(ctx, *, message=None):
    message = message
    if message == None:
        await ctx.send(f'yo, you needa tell me what you want this command to say for it to work **({prefix}say4me <message>)**')
    else:
        await ctx.message.delete()
        await ctx.send(message)

@bot.command(name='say4meDM')
async def _sayformeDM(ctx, *, message=None):
    message = message
    if message == None:
        await ctx.send(f'yo, you needa tell me what you want this command to say for it to work **({prefix}say4medm <message>)**')
    else:
        await ctx.send(message)

@bot.command(name='gimmenumber')
async def _gimmenumber(ctx):
    x = str(randint(1,500))
    await ctx.send(x)


@bot.command(name='coinflip')
async def _coinflip(ctx):
    x = randint(1,2)
    if x == 2:
        await ctx.send('Tails!')
    if x == 1:
        await ctx.send('Heads!')










@bot.command(name='yeetedpeeps')
async def _bannedpeople(ctx):
    guild = ctx.guild

    embed=discord.Embed(color=success_color)
    TheYeeted = await guild.bans()
    for ban in TheYeeted:
        embed.add_field(name=f"User: `{ban.user.name}#{ban.user.discriminator}`", value=f"Reason: `{ban.reason}`", inline=False)
    embed.set_author(name='Banned user list')
    await ctx.send(embed=embed)




    



@bot.command(name='depression',aliases=['dhelp', 'suicide', 'suicidal','kms','depressionhelp'])
async def _depressionhelp(ctx):
    await ctx.send(f'There\'s help, {ctx.author.mention}!\n :flag_us: 1-800-273-8255\n :flag_ru: (7) 0942 224 621\n :flag_ca: 1-800-668-6868\n :flag_cn: 0800-810-1117')


@bot.command(name='pp')
async def _ppsize(ctx):
    sizes = [
        '8==D',
        '8=D',
        '8==============D',
        '8=====D',
        '8D',
        '8================================D'
    ]
    size=randint(0,6)
    embed=discord.Embed(color=success_color)
    embed2=discord.Embed(color=success_color)
    if ctx.message.author.id == 802280775084015616:
        embed2.add_field(name=f"{ctx.message.author}'s pp size!", value='8===================================================================================================================================================D')
        await ctx.send(embed=embed2)
    if ctx.message.author.id != 802280775084015616:
        embed.add_field(name=f"{ctx.message.author}'s pp size!", value=f"{sizes[size]}", inline=False)
        await ctx.send(embed=embed)







@bot.command(name='deletus')
async def _deletus(ctx, *, arg1=None, arg2=None):
    if ctx.author.guild_permissions.administrator == True:
        if arg1 == None:
            embed3=discord.Embed(title="bruh that\'s not how it works...", description="bruh, my man, you need to give me a number of messages to deletus", color=fail_color)
            await ctx.send(embed=embed3)

        if arg1 == 'my penis':
            await ctx.reply("Your penis has been deletused, go look. Oh.. wait... It's not deletused, it's just to small for me to see!")

        pp = int(arg1) + 1
        embed=discord.Embed(title=f"Deletus!", description=f"{pp} messages deletussed", color=success_color)

        await ctx.channel.purge(limit=int(pp))
        await ctx.send(embed=embed)



    if ctx.author.guild_permissions.administrator == False:
        embed2=discord.Embed(title=f"nah man ", description=f"nah, **`{ctx.author.name}#{ctx.author.discriminator}`**, I\'m good.", color=fail_color)
        await ctx.send(embed=embed2)

@bot.command(name='changemyname')
async def _hidemyass(ctx, *, arg1=None):
    embed=discord.Embed(title=f'**Nick Reset** 👌', description=f'nick reset for **`{ctx.author.name}#{ctx.author.discriminator}`**', color=success_color)
    embed2=discord.Embed(title=f'**Nick Changed** 👌', description=f'nick changed for **`{ctx.author.name}#{ctx.author.discriminator}`** to  **`{arg1}`**', color=success_color)

    if arg1 == None:
        await discord.Member.edit(nick=ctx.author.name,self=ctx.author)
        await ctx.send(embed=embed)

    else:
        await discord.Member.edit(nick=arg1,self=ctx.author)
        await ctx.send(embed=embed2)
    








@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_author_discriminator
    global snipe_message_author_profilepicture
    # Variables outside a function have to be declared as global in order to be changed

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_author_discriminator = message.author.discriminator
    snipe_message_author_profilepicture = message.author.avatar_url
    await asyncio.sleep(60)
    snipe_message_author = None
    snipe_message_content = None
    snipe_message_author_discriminator = None
    snipe_message_author_profilepicture = None
    
@bot.command(name='snipem')
async def _snipe(message):

    if snipe_message_content==None:
        await message.channel.send("Ayo ayo ayo ayo chill man, sheesh you must be hallucinating")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Here ya go, chief {message.author.name}#{message.author.discriminator}", icon_url=snipe_message_author_profilepicture)
        embed.set_author(name= f"@{snipe_message_author}#{snipe_message_author_discriminator}")
        await message.channel.send(embed=embed)
        return

@bot.command(name='yeet')
async def _ban(ctx:commands.Context, member:discord.User=None, *, reason=None):
    if ctx.author.guild_permissions.ban_members == True:
        embed=discord.Embed(title=f"{member} yeeted!", description=f"Yeeted for reason: `{reason}`", color=success_color)
        if member == None or member == 871584632628465726: # The tag given is so the user can't make the bot ban itself.
            embed3=discord.Embed(title=f"You gotta give me someone...", description=f"{prefix}ban (member) (reason)", color=fail_color)
            await ctx.send(embed=embed3)
        if reason == None:
            await ctx.send('bruh add a reason')
        else:
            await member.send(reason)
            await ctx.send(embed=embed)

            await asyncio.sleep(1)
            await ctx.guild.ban(user=member,reason=reason)
    else:
        embed2=discord.Embed(description=f"`{ctx.message.author.name}`", color=fail_color)
        embed2.set_author(name=f'This man tried to ban {member}!',icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed2)

@bot.command(name='kick')
async def _kick(ctx, member:discord.User=None):
    if ctx.author.guild_permissions.kick_members == True:
        if member == None or member == ctx.message.author or member == 871584632628465726: # The tag given here is the tag for the default robot, you will have to change it for yours. It just makes sure nobody tries to kick/ban the bot using itself.
            embeddidntkick=discord.Embed(title="That's not how it works...", description="You can't kick yourself or nobody.", color=fail_color)
            await ctx.send(embed=embeddidntkick)
        else:
            await ctx.guild.kick(member)
            await ctx.send('kicked them!')
    else:
        await ctx.send(f'ayo ayo tf man you can\'t kick someone,`{ctx.message.author}`')





@bot.command(name='unyeet')
async def _unyeet(ctx, *, member):
    if ctx.author.guild_permissions.ban_members == True:
        embed=discord.Embed(title="👌 unbanned", description=f'`{member}`', color=success_color)
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for banentry in banned_user:
            user = banentry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)
                return
    else:
        embed=discord.Embed(color=fail_color)
        embed.set_author(name=f'{ctx.message.author} tried to unban someone!', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)


    






@bot.command(name='roles')
async def _roles(ctx):
    if ctx.author.guild_permissions.manage_roles == True:
        embed=discord.Embed(title="A list of all roles, my good man", description=':)', color=success_color)
        for r in ctx.guild.roles:
            embed.add_field(name=f"{r.name}", value=f"{r.permissions}", inline=False)

        await ctx.send(embed=embed)
    
    if ctx.author.guild_permissions.manage_roles == False:
        failembed=discord.Embed(title=f"I\'m sorry...", description=f"sorry, `{ctx.author.name}#{ctx.author.discriminator}`, but nah.", color=fail_color)
        await ctx.send(embed=failembed)




@bot.command(name='memez')
async def _memez(ctx):
    embed = discord.Embed(title=f"here ya go {ctx.author.name}@{ctx.author.discriminator}", description="", color=success_color)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randrange(0, 25)]['data']['url'])
            await ctx.send(embed=embed)






@bot.command(name='reddit')
async def _reddit(ctx, reddit):
    embed = discord.Embed(title=f"here ya go {ctx.author.name}@{ctx.author.discriminator}", description="", color=success_color)

    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{reddit}/new.json?') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randrange(0, 25)]['data']['url'])
            await ctx.send(embed=embed)





#start of music player
import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('Bruh, this command isn\'t for DM\'s.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('!!!SEVERE BRUH MOMENTO!!!\nDiagnosis: {}\nRecommended action: Stop being a turd.'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """
        if ctx.message.author.id == 802280775084015616 or ctx.message.author.guild_permissions.manage_guild:
            if not channel and not ctx.author.voice:
                raise VoiceError('Uh, chief? I can\'t find you. You didn\'t even tell me a channel to join either bruh.')

            destination = channel or ctx.author.voice.channel
            if ctx.voice_state.voice:
                await ctx.voice_state.voice.move_to(destination)
                return

            ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""
        if ctx.message.author.guild_permissions.manage_guild:
            if not ctx.voice_state.voice:
                return await ctx.send('Bruh. Does it look, like I\'m in a voice channel? No, it doesn\'t. So why are you telling me to leave? Turd.')

            await ctx.voice_state.stop()
            del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Ayo bruh momento, nothing\'s playing on our super epic genius radio.')

        if 0 > volume > 100:
            return await ctx.send('Pick a number, any number (preferrably between 0 and 100)!')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%.. not like this feature works though.'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""
        if ctx.message.author.guild_permissions.manage_guild or ctx.message.author == Song.requester:
            if ctx.voice_state.voice.is_playing():
                ctx.voice_state.voice.pause()
                await ctx.message.add_reaction('👌')

    @commands.command(name='resume')
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""
        if ctx.message.author.guild_permissions.manage_guild or ctx.message.author == Song.requester:
            if ctx.voice_state.voice.is_paused():
                ctx.voice_state.voice.resume()
                await ctx.message.add_reaction('👌')

    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        if ctx.message.author.guild_permissions.manage_guild:
            """Stops playing song and clears the queue."""

            ctx.voice_state.songs.clear()

            if not ctx.voice_state.is_playing:
                ctx.voice_state.voice.stop()
                await ctx.message.add_reaction('👌')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Severe bruh momento, you can\'t expect me to simply skip a non-existent song')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('👌')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('👌')
                ctx.voice_state.skip()
            else:
                await ctx.send('ight bruh your vote\'s counted, skip votes at **{}/3**'.format(total_votes))

        else:
            await ctx.send('Bruh this ain\'t an election, you can\'t rig the voting.')
            await ctx.message.add_reaction('🗿')

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            await ctx.send('Bruh my man you gotta make a list of songs to play')
            await ctx.message.add_reaction('🗿')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} singey songs bruh:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('👌')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            await ctx.send('Empty queue.')
            await ctx.message.add_reaction('🗿')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('👌')

    @commands.command(name='tts')
    async def _tts(self, ctx, *, message):
        if not ctx.voice_state.is_playing and ctx.author.voice:
            while os.system(f'espeak -s 150 -w "h.mp3" "{message}"'):
                await asyncio.sleep(1)
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('h.mp3')
            player = voice.play(source)
            await ctx.message.add_reaction('👌')
            player
            while voice.is_playing():
                await asyncio.sleep(1)
            await ctx.voice_client.disconnect()
    
    @commands.command(name='laugh')
    async def _laugh(self, ctx):
        if ctx.author.voice:
            channela = ctx.message.author.voice.channel
            voik = await channela.connect()
            sauce = FFmpegPCMAudio('laugh.mp3')
            playah = voik.play(sauce)
            playah
            while voik.is_playing():
                await asyncio.sleep(1)
            await ctx.voice_client.disconnect()



    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('Ayo ayo ayo bruh somethin\' wrong happen: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Ight bruh, this yo song? {}'.format(str(source)))
                await ctx.message.add_reaction('👌')

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')


bot.add_cog(Music(bot))
#end of music player















bot.run(token)
