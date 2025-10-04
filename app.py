#!/usr/bin/env python3
import json
import random
import string
import asyncio
import aiohttp
from pathlib import Path


NICKNAME_BASE = "Inazuma" #Here Your Name
ACCOUNTS_FILE = Path("guest-accounts.json")
API_URL = "http://changenamedat.onrender.com/change"
MAX_CONCURRENT = 10  
TIMEOUT_SECONDS = 15

# ---------------- FUNCTIONS ----------------
def generate_name(base_name=NICKNAME_BASE, total_length=12):
    """Génère un pseudo aléatoire avec un suffixe."""
    max_base_length = total_length - 2
    base_part = base_name[:max_base_length]
    random_part = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=total_length - len(base_part) - 1
    ))
    return f"{base_part}_{random_part}"

def load_tokens(filename=ACCOUNTS_FILE):

    if not filename.is_file():
        raise FileNotFoundError(f"Token file not found: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

async def change_name(session, uid, password, new_name, index, sem):
 
    async with sem:
        try:
            async with session.get(API_URL, params={
                "uid": uid,
                "password": password,
                "new_name": new_name
            }, timeout=TIMEOUT_SECONDS) as resp:

                if resp.status == 200:
                    print(f"[{index}] ✅ New Nickname: {new_name} (Status: {resp.status})")
                else:
                    try:
                        data = await resp.json()
                        error_message = data.get("error", "Unknown error")
                    except Exception:
                        error_message = await resp.text()
                    print(f"[{index}] ❌ ERROR for UID {uid} - Message: {error_message}")

        except asyncio.TimeoutError:
            print(f"[{index}] ❌ Timeout for UID {uid}")
        except aiohttp.ClientError as e:
            print(f"[{index}] ❌ Request error for UID {uid}: {e}")

async def main():
    tokens_data = load_tokens()
    sem = asyncio.Semaphore(MAX_CONCURRENT)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for idx, entry in enumerate(tokens_data, start=1):
            uid = entry.get("uid")
            password = entry.get("password")
            if uid and password:
                new_name = generate_name()
                tasks.append(change_name(session, uid, password, new_name, idx, sem))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())


