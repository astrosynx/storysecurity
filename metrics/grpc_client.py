import grpc
import time

# placeholder imports — Story protobufs
# from story.proto.node_pb2 import StatusRequest
# from story.proto.node_pb2_grpc import NodeStub

class StoryGRPCClient:
    def __init__(self, endpoint="localhost:9090"):
        self.endpoint = endpoint

    def collect(self):
        # NOTE: here intentionally lightweight and safe
        data = {
            "grpc_reachable": False,
            "block_height": None,
            "syncing": None,
            "timestamp": time.time()
        }

        try:
            channel = grpc.insecure_channel(self.endpoint)
            grpc.channel_ready_future(channel).result(timeout=2)

            # stub = NodeStub(channel)
            # status = stub.Status(StatusRequest())

            # mocked values until proto binding
            data["grpc_reachable"] = True
            data["block_height"] = 123456
            data["syncing"] = False

        except Exception as e:
            data["error"] = str(e)

        return data
