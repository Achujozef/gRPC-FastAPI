from fastapi import FastAPI, Request
import grpc
from user_service_pb2 import GetUserRequest
from user_service_pb2_grpc import UserServiceStub
import uvicorn
app2 = FastAPI()
client = grpc.insecure_channel('localhost:50051')  # Replace with the address of the first microservice

def get_user(user_id):
    stub = UserServiceStub(client)
    request = GetUserRequest(user_id=user_id)
    response = stub.GetUser(request)
    return response.username

@app2.get("/get_user/{user_id}")
def get_user_info(user_id: str):
    username = get_user(user_id)
    return {"Username": username}

if __name__ == "__main__":

    uvicorn.run(app2, host="0.0.0.0", port=8001)