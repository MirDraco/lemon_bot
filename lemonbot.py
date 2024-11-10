import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 접근 권한 활성화
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# 슬래시 커맨드 예제
@bot.tree.command(
    name="안녕", 
    description="레몬룡이 인사해줌",
 
    )
async def 안녕(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name}님 안녕!")


@bot.tree.command(
    name="바보", 
    description="레몬룡이 바보라고 함",
 
    )
async def 바보(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name}님 바보!")

@bot.tree.command(
    name="hentai", 
    description="레몬룡이 사용자에게 변태라고 함",
 
    )
async def hentai(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name}님 변태!")


# 슬래시 커맨드를 동기화하는 코드
@bot.event
async def on_ready():
    await bot.tree.sync()  # 커맨드를 서버에 동기화
    print(f"Synced slash commands for {bot.user}.")


bot.run("")
