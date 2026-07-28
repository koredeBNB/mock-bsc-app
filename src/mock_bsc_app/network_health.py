from __future__ import annotations


def get_network_health(network: str) -> dict[str, object]:
    """Return network health data for documentation update demos."""
    return {
        "network": network,
        "status": "healthy",
        "peer_count": 64,
        "rpc_latency_ms": 42,
        "latest_block": 39126100,
    }
