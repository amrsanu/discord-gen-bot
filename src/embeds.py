import discord
from src.discord_main import client
from src.discord_main import _logger


@client.command(pass_context=True, brief="Define embeds to have a embed message")
async def embed(context):
    """Can define embed based on any message or so
    This embed defines sample embed."""
    try:
        embed = discord.Embed(
            title="Rules!",
            url="https://www.google.com/",
            description="Rules and Regulations.",
            color=0x4DFF4D,
        )
        embed.set_author(
            name="Amrendra Pratap Singh",
            # name=context.author.display_name, icon_url=context.author.avatar_url,
            url="https://www.linkedin.com/in/amrsanu/",
            icon_url="https://avatars.githubusercontent.com/u/22052268?s=400&u=82a78058c24cf9931f2fcf69ff75db550bff898c&v=4",
        )
        embed.set_thumbnail(
            url="https://media.licdn.com/dms/image/C4E16AQErSZb7bqOZiA/profile-displaybackgroundimage-shrink_350_1400/0/1596190618751?e=1683763200&v=beta&t=_-vtoJ5zr3VxJiseJtwk8ten1JOdc8u8MIxH-4bAJfA"
        )
        embed.add_field(name="Disclamer!", value="Check the disclamer.", inline=True)
        # inline=Ture - will put all the fields in a same line.
        embed.add_field(name="About!", value="About the Author.", inline=True)
        embed.set_footer(text="Thank you for joining the Server.")
        await context.send(embed=embed)
    except Exception as ex:
        msg = f"Command error: {ex}"
        await context.send(msg)
    finally:
        _logger("embed", msg, context.author.mention)
