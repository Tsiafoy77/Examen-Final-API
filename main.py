from fastapi import FastAPI

app = FastAPI()
phones_db=[]
Characteristic={
    ram_memory: int,
    rom_memory: int
}
class phones(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristic



@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/health")
def health():
    return "OK"

@app.post("/phones",status_code=200)
async def create_phones(phones:List[phones]):
    phones_db.extend(posts)
    return phones_db
