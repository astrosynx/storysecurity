import psutil

class RuntimeMetrics:
    def __init__(self):
        self.start_peers = self.peers()

    def peers(self):
        return len(psutil.net_connections())

    def finish(self, duration):
        end_peers = self.peers()
        data = {
            "duration_sec": round(duration, 2),
            "peers_before": self.start_peers,
            "peers_after": end_peers,
        }
        print("[METRICS]", data)
        return data
