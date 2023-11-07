from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import grpc
from concurrent import futures
from user_service_pb2 import GetUserResponse, GetUserRequest
from user_service_pb2_grpc import add_UserServiceServicer_to_server, UserServiceServicer
import uvicorn
app = FastAPI()

class UserService(UserServiceServicer):
    def GetUser(self, request, context):
        user_id = request.user_id
        # Fetch user information based on the user_id
        # For this example, return a dummy response
        return GetUserResponse(username=f"User_{user_id}")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
add_UserServiceServicer_to_server(UserService(), server)

@app.post("/grpc_endpoint")
def grpc_endpoint(request: Request):
    data = server.invoke_unary_unary(request.body, 10)
    return JSONResponse(data)

if __name__ == "__main__":
    server.add_insecure_port('[::]:50051')  # gRPC server listens on port 50051
  # gRPC server listens on port 50051
    server.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
