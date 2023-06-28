from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel

import config
from employers.models import EmployersDAO
from logger import logger

router = APIRouter(prefix="/employers", tags=["Заказчики"])

bot_tokens = config.settings.bot_tokens


class Data(BaseModel):
    phone: Optional[str]
    user_id: Optional[str]
    bot_token: str


def check_token(data: Data):
    try:
        bot_token = data.dict()["bot_token"]
        if bot_token not in bot_tokens:
            raise HTTPException(status_code=403, detail="Not authorized")
    except KeyError:
        raise HTTPException(status_code=403, detail="Not authorized")
    res = {k: v for k, v in data.dict().items() if k != "bot_token"}
    res = {k: v for k, v in res.items() if v is not None}
    return res


@router.post("/get", status_code=200)
async def read_one_employer(data: Data):
    res = check_token(data=data)
    employer = await EmployersDAO.read_one_or_none(**res)
    if employer:
        return employer
    raise HTTPException(status_code=404, detail="Item not found")

