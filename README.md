# DISCORD GEN BOT

## Features

- Commands to invoke multiple APIs
  - Query chatgpt, $gpt [query]
  - Get daily quotes, $quote
  - Get daily jokes, $joke
- Other commands
  - Invite users to Voice channel, $send_invite <mention_user>
  - Invite the BOT to the Voice channel, $invite_voice
  - Remove the BOT from the Voice channel, $leave_voice
  - Play Music, $play <song_num>
  - Pause Music, $pause
  - Resume Music, $resume 
  - Stop Music, $stop
  - Queue Music, $queue <song_num>
  - Send direct message to server users, $message <mention user> [message]
  - Add personalized embeds in the chat, $embed
- Managing the users in cannel.
  - Kick users,
  - Ban users, 
- Events
  - When user joins/leaves the channel - BOT greets with a message and banner.
  - On message from user
    - Bot will check for ABUSIVE/SEWEAR/BAD words, warns the user by deleting the message.

## Requirements

- Python Packages
  - discord
  - discord.py[voice]
  - openai
  - services
  - requests

## Setting up the Discord Developer Application

- Goto <https://discord.com/developers>
  - Create new Application
  - Give a suitable name
- Goto Bot tab - Add Bot

## Packages

- Install using below commands
  - pip install -U discord
  - pip install -U discord.py[voice]

## Other Binaries

- Download and install FFMpeg <https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip>
