from __future__ import annotations

from mock_bsc_app.network_health import get_network_health


def test_get_network_health_returns_documented_fields() -> None:
    health = get_network_health("bnb-smart-chain")

    assert health == {
        "network": "bnb-smart-chain",
        "status": "healthy",
        "peer_count": 64,
        "rpc_latency_ms": 42,
        "latest_block": 39126100,
    }
