import os
from routers.huawei import Ax3
from routers.zyxel import VMG8924

def get_router(router_type: str) -> Ax3:

    host = os.getenv('ROUTER_HOST')
    user = os.getenv('ROUTER_USER')
    password = os.getenv('ROUTER_PASSWORD')

    match router_type:
        case "ax3":
            return Ax3(host, user, password)
        case "vmg8924":
            return VMG8924(host, user, password)
        case _:
            raise ValueError(f"Router type {router_type} not supported")