from __future__ import annotations

from mock_bsc_app.gas_fees import get_gas_fee_status


def test_get_gas_fee_status_returns_documented_fields() -> None:
    status = get_gas_fee_status("bnb-smart-chain")

    assert status == {
        "network": "bnb-smart-chain",
        "base_fee_gwei": 3.2,
        "priority_fee_gwei": 0.8,
        "estimated_total_fee_gwei": 4.0,
        "congestion_level": "low",
        "sample_block": 39124801,
    }
