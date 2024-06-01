from discord import Intents
from discord.ext import commands
from siegeapi import Auth

from DataSource.DiscordToken import TOKEN

intents = Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

token = TOKEN


async def fetch_siege_data(player_name):
    auth = Auth('danilod0129@outlook.com', 'Eyleen0129#')
    player = await auth.get_player(name=player_name)
    output = []
    output.append(f"Name: {player.name}")
    output.append(f"Profile pic URL: {player.profile_pic_url}")

    await player.load_persona()
    output.append(f"Streamer nickname: {player.persona.nickname}")
    output.append(f"Nickname enabled: {player.persona.enabled}")

    await player.load_playtime()
    output.append(f"Total Time Played: {player.total_time_played:,} seconds / {player.total_time_played_hours:,} hours")
    output.append(f"Level: {player.level}")

    await player.load_ranked_v2()
    output.append(f"Ranked Points: {player.ranked_profile.rank_points}")
    output.append(f"Rank: {player.ranked_profile.rank}")
    output.append(f"Max Rank Points: {player.ranked_profile.max_rank_points}")
    output.append(f"Max Rank: {player.ranked_profile.max_rank}")

    await player.load_progress()
    output.append(f"XP: {player.xp:,}")
    output.append(f"Total XP: {player.total_xp:,}")
    output.append(f"XP to level up: {player.xp_to_level_up:,}")

    await auth.close()
    return "\n".join(output)


@bot.command(name='siege')
async def siege_info(ctx, *, player_name: str = None):
    if not player_name:
        await ctx.send("Please provide a player name. Usage: `!siege [player_name]`")
        return

    try:
        response = await fetch_siege_data(player_name)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


bot.run(TOKEN)
