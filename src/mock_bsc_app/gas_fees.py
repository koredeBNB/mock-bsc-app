from __future__ import annotations


def get_gas_fee_status(network: str) -> dict[str, object]:
    """Return current gas fee information for documentation update demos."""
    return {
        "network": network,
        "base_fee_gwei": 3.2,
        "priority_fee_gwei": 0.8,
        "estimated_total_fee_gwei": 4.0,
        "congestion_level": "low",
        "sample_block": 39124801,
    }
