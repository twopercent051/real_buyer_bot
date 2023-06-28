from fastapi import FastAPI

from employers.router import router as employers_router


app = FastAPI(title="real_buyer_bot")

app.include_router(employers_router)
