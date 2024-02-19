#!/bin/bash

bot=$(python -c "import base64; print(base64.b64encode(open('bot.py', 'rb').read()).decode())")
req=$(python -c "import base64; print(base64.b64encode(open('requirements.txt', 'rb').read()).decode())")

sed -i "s/bot.py:.*/bot.py: $bot/g" kubernetes/bot/discord-bot/bot-cm.yaml
sed -i "s/requirements.txt:.*/requirements.txt: $req/g" kubernetes/bot/discord-bot/bot-cm.yaml
