import discord
import os
import json
from discord.ext import commands
from typing import Literal
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='k!', intents=intents)

points_file = 'housepoints.json'

def load_points():
    if os.path.exists(points_file):
        with open(points_file, 'r') as f:
            return json.load(f)
    return {"Slytherin": 0}

def save_points(points):
    with open(points_file, 'w') as f:
        json.dump(points, f)

@bot.event
async def on_ready():
    print('PointsBot Ready!')

@bot.command()
#@commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def s(ctx, give_take: Literal['give', 'take'], amount: int, *, reason):
    points = load_points()
    house = 'Slytherin'
    if give_take == 'give':
        points[house] = points.get(house, 0) + amount
        await ctx.send(f'Gave Slytherin {amount} points for {reason}')
    elif give_take == 'take':
        points[house] = points.get(house, 0) - amount
        await ctx.send(f'Took {amount} points from Slytherin for {reason}')
    save_points(points)
  
@bot.command()
#@commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def r(ctx, give_take: Literal['give', 'take'], amount: int, *, reason):
    points = load_points()
    house = 'Ravenclaw'
    if give_take == 'give':
        points[house] = points.get(house, 0) + amount
        await ctx.send(f'Gave Ravenclaw {amount} points for {reason}')
    elif give_take == 'take':
        points[house] = points.get(house, 0) - amount
        await ctx.send(f'Took {amount} points from Ravenclaw for {reason}')
    save_points(points)

@bot.command()
#@commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def g(ctx, give_take: Literal['give', 'take'], amount: int, *, reason):
    points = load_points()
    house = 'Gryffindor'
    if give_take == 'give':
        points[house] = points.get(house, 0) + amount
        await ctx.send(f'Gave Gryffindor {amount} points for {reason}')
    elif give_take == 'take':
        points[house] = points.get(house, 0) - amount
        await ctx.send(f'Took {amount} points from Gryffindor for {reason}')
    save_points(points)

@bot.command()
#@commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def h(ctx, give_take: Literal['give', 'take'], amount: int, *, reason):
    points = load_points()
    house = 'Hufflepuff'
    if give_take == 'give':
        points[house] = points.get(house, 0) + amount
        await ctx.send(f'Gave Hufflepuff {amount} points for {reason}')
    elif give_take == 'take':
        points[house] = points.get(house, 0) - amount
        await ctx.send(f'Took {amount} points from Hufflepuff for {reason}')
    save_points(points)

@bot.command()
@commands.has_role('myself') #SWAP WITH ADMIN BEFORE DEPLOYMENT
async def resetpoints(ctx):
  await ctx.send("Are you sure you want to run this command? (yes/no)")
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
  try:
      response = await bot.wait_for('message', check=check, timeout=30.0)
  except asyncio.TimeoutError:
      return
  if response.content.lower() not in ("yes", "y"):
      return
  points = load_points()
  for house in points:
      points[house] = 0
  save_points(points)
  await ctx.send('Points reset!')

@bot.command()
async def housepoints(ctx):
  points = load_points()
  await ctx.send(f'Gryffindor: {points["Gryffindor"]} point(s)\nHufflepuff: {points["Hufflepuff"]} point(s)\nRavenclaw: {points["Ravenclaw"]} point(s)\nSlytherin: {points["Slytherin"]} point(s)')

bot.run(os.environ['TOKEN'])