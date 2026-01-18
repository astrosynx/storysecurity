from faults.network.latency import NetworkLatency
from faults.network.packet_loss import PacketLoss
from faults.node.restart import NodeRestart

FAULTS = {
    "network.latency": NetworkLatency(),
    "network.packet_loss": PacketLoss(),
    "node.restart": NodeRestart(),
}
