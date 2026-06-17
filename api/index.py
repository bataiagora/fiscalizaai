
from telegram import Bot
import asyncio

TOKEN = "SEU_TOKEN_DO_BOT"
CHAT_ID = -1004470036770

async def enviar():
bot = Bot(token=TOKEN)

```
await bot.send_message(
    chat_id=CHAT_ID,
    text="🚀 FiscalizaAi conectado ao Vercel com sucesso!"
)
```

def handler(request):
asyncio.run(enviar())
return {
"statusCode": 200,
"body": "OK"
}
