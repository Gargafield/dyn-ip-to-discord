from routers.huawei import Ax3
from routers.zyxel import VMG8924

def get_router(router_type: str) -> Ax3:
    match router_type:
        case "ax3":
            return Ax3()
        case "vmg8924":
            return VMG8924()
        case _:
            raise ValueError(f"Router type {router_type} not supported")