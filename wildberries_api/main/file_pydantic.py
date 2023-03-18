from pydantic import BaseModel,Field


class Brand_box(BaseModel):
    no_return_map: int
    brand_name: str
    supplier_id: int


class Data_py(BaseModel):
    name: str=Field(alias='imt_name')
    article: int=Field(alias='nm_id')
    brand_name: Brand_box=Field(alias='selling')


