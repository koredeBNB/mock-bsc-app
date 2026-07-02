from __future__ import annotations


def get_gas_fee_status(network: str) -> dict[str, object]:
    """Return current gas fee information for documentation update demos."""
    return {
        "network": network,
        "base_fee_gwei": 3.5,
        "priority_fee_gwei": 1.1,
        "estimated_total_fee_gwei": 4.6,
        "congestion_level": "medium",
        "sample_block": 39126000,
        "fee_trend": "rising",
    }
