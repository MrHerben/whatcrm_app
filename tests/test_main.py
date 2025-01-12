import aiohttp
import pytest
import sys
import os
# Добавляем папку `app` в sys.path, чтобы pytest не ругался
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from config import Config

@pytest.fixture
async def client():
    async with aiohttp.ClientSession() as session:
        yield session

async def test_tariffs(client):
    async with client.get(f"http://{Config.HOST}:{Config.PORT}") as response:
        assert response.status == 200  # Проверяем статус ответа
