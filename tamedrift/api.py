from ninja import NinjaAPI

from wildrift_cn.api import router as wildrift_cn_router

api = NinjaAPI(title="Tamed Rift")

api.add_router("/wildrift_cn/", wildrift_cn_router)
