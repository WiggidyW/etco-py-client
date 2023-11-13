import etco_pb2

class ProtoUnauthorized(Exception):
    def __init__(self):
        super().__init__("ProtoUnauthorized")

def raise_if_unauthorized(auth: etco_pb2.AuthResponse):
    if not auth.authorized:
        raise ProtoUnauthorized()

class ProtoErrorResponse(Exception):
    def __init__(
        self,
        code: etco_pb2.ErrorCode,
        error: str,
    ):
        super().__init__(f"ProtoErrorResponse: {code}: {error}")
        self.code = code
        self.error = error

def raise_if_err(error: etco_pb2.ErrorResponse):
    if error.code != etco_pb2.OK:
        raise ProtoErrorResponse(error.code, error.error)