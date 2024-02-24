from .app_constant import AppErrorMessages


class AppUtils:
    def formatAppResponse(
        code=AppErrorMessages.OK, message=AppErrorMessages.OK, data=""
    ):
        return {"code": code, "message": message, "data": data}
