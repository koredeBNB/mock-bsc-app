from __future__ import annotations

from mock_bsc_app.block_sync import get_block_sync_status


def test_get_block_sync_status_returns_documented_fields() -> None:
    status = get_block_sync_status("bnb-smart-chain")

    assert status == {
        "network": "bnb-smart-chain",
        "latest_block": 39126000,
        "safe_block": 39125920,
        "finalized_block": 39125810,
        "sync_lag_blocks": 80,
        "is_syncing": False,
        "sync_mode": "full",
    }
