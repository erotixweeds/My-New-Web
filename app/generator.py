import random
from fastapi import APIRouter
from db import get_db


router = APIRouter()


wordlists = {
	"HOTMAIL LINKED NF": "Netflix_wordlist.txt",
	"HBO": "hbo_wordlist.txt",
    "crunchyroll": "crunchyroll_wordlist.txt",
    "mixed": "mixed_wordlist.txt",
    "EXPRESS VPN": "Express_wordlist.txt",
    "Hotmail LQ": "Hotmail_wordlist.txt",
}


@router.get("/generate/{service}")
def generate(service: str):
if service not in wordlists:
return {"error": "Invalid service"}


with open(wordlists[service]) as f:
data = [x.strip() for x in f if x.strip()]


word = random.choice(data)


db = get_db()
db.execute("UPDATE generation_count SET count=count+1")
db.commit()


return {"generated": word}
