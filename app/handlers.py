from aiohttp import web
import aiohttp
from config import Config

# Получение запроса, создание своего и возврат ответа инициатору первого запроса
async def get_tariffs(request):
    headers = {
        "X-Whatsapp-Token": Config.TOKEN
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(Config.BASE_URL+"/v3/tariffs", params=Config.PARAMS, headers=headers) as response:
                if response.status != 200:
                    raise web.HTTPBadRequest(reason=f"API error: {await response.text()}")
                data = await response.json()
                return web.json_response(data)
        except aiohttp.ClientError as e:
            raise web.HTTPInternalServerError(reason=f"Request failed: {e}")
