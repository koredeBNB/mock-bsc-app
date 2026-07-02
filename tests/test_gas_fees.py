from __future__ import annotations

from mock_bsc_app.gas_fees import get_gas_fee_status


def test_get_gas_fee_status_returns_documented_fields() -> None:
    status = get_gas_fee_status("bnb-smart-chain")

    assert status == {
        "network": "bnb-smart-chain",
        "base_fee_gwei": 3.5,
        "priority_fee_gwei": 1.1,
        "estimated_total_fee_gwei": 4.6,
        "congestion_level": "medium",
        "sample_block": 39126000,
        "fee_trend": "rising",
    }
