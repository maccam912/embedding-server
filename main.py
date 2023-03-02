from pydantic.dataclasses import dataclass
import uform
from starlite import Starlite, post

@dataclass
class Req:
    text: str

@dataclass
class Res:
    embedding: list[float]

model = uform.get_model("unum-cloud/uform-vl-english")

@post(path="/text")
async def text_embedding(data: Req) -> Res:
    text_data = model.preprocess_text(data.text)
    text_embedding = model.encode_text(text_data)
    np_embed: list[float] = text_embedding.detach().numpy().tolist()[0]
    response = Res(embedding=np_embed)
    # 256 numbers long
    return response


app = Starlite(route_handlers=[text_embedding])
