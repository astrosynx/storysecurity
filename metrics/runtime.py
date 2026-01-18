import psutil
from metrics.grpc_client import StoryGRPCClient

class RuntimeMetrics:
    def __init__(self):
        self.start_peers = self.peers()
        self.grpc = StoryGRPCClient()

    def peers(self):
        return len(psutil.net_connections())

    def finish(self, duration):
        end_peers = self.peers()
        grpc_metrics = self.grpc.collect()

        data = {
            "duration_sec": round(duration, 2),
            "peers_before": self.start_peers,
            "peers_after": end_peers,
            "grpc": grpc_metrics
        }

        print("[METRICS]", data)
        return data
