from concurrent import futures
import logging
import grpc
from db_commands import MyDB
import users_pb2
import users_pb2_grpc
db = MyDB()


class Users(users_pb2_grpc.UsersServicer):
    def GetUsers(self,request,context):
        users = []
        print(db.get_users())
        for i in db.get_users():
            users.append(users_pb2.User(id="1",name=i[0] ,email=i[1],password=i[2]))
        return users_pb2.GetUsersResponse(users= users)
    def CreateUser(self,request,context):
        
        db.create_user(request.user.id,
                    request.user.name,
                    request.user.email,
                    request.user.password)
        return  users_pb2.CreateUserResponse(  user = users_pb2.User(id=request.user.id,name=request.user.name ,email=request.user.email,password=request.user.password))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
