from siegeapi import Auth
import asyncio

async def sample():
    auth = Auth('danilod0129@outlook.com', 'Eyleen0129#')
    player = await auth.get_player(name="Microsoft.365")

    print(f"Name: {player.name}")
    print(f"Profile pic URL: {player.profile_pic_url}")

    await player.load_persona()
    print(f"Streamer nickname: {player.persona.nickname}")
    print(f"Nickname enabled: {player.persona.enabled}")

    await player.load_playtime()
    print(f"Total Time Played: {player.total_time_played:,} seconds / {player.total_time_played_hours:,} hours")
    print(f"Level: {player.level}")

    await player.load_ranked_v2()
    print(f"Ranked Points: {player.ranked_profile.rank_points}")
    print(f"Rank: {player.ranked_profile.rank}")
    print(f"Max Rank Points: {player.ranked_profile.max_rank_points}")
    print(f"Max Rank: {player.ranked_profile.max_rank}")

    await player.load_progress()
    print(f"XP: {player.xp:,}")
    print(f"Total XP: {player.total_xp:,}")
    print(f"XP to level up: {player.xp_to_level_up:,}")

    await auth.close()

asyncio.run(sample())
