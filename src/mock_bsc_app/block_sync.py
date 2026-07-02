from __future__ import annotations


def get_block_sync_status(network: str) -> dict[str, object]:
    """Return block synchronization status for documentation update demos."""
    return {
        "network": network,
        "latest_block": 39126000,
        "safe_block": 39125920,
        "finalized_block": 39125810,
        "sync_lag_blocks": 80,
        "is_syncing": False,
    }
