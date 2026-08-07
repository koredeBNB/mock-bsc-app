from __future__ import annotations

import pytest

from mock_bsc_app.gas_fees import estimate_blob_fee, get_gas_fee_status


def test_get_gas_fee_status_returns_documented_fields() -> None:
    status = get_gas_fee_status("bnb-smart-chain")

    assert status == {
        "network": "bnb-smart-chain",
        "base_fee_gwei": 3.5,
        "priority_fee_gwei": 1.1,
        "estimated_total_fee_gwei": 4.6,
        "blob_base_fee_gwei": 0.25,
        "max_fee_per_gas_gwei": 8.0,
        "congestion_level": "medium",
        "sample_block": 39126000,
        "fee_trend": "rising",
    }


def test_estimate_blob_fee_scales_with_blob_count() -> None:
    estimate = estimate_blob_fee(4, "bnb-smart-chain")
    assert estimate == {
        "network": "bnb-smart-chain",
        "blob_count": 4,
        "blob_base_fee_gwei": 0.25,
        "estimated_blob_fee_gwei": 1.0,
        "sample_block": 39126000,
    }


def test_estimate_blob_fee_rejects_non_positive_count() -> None:
    with pytest.raises(ValueError, match="blob_count"):
        estimate_blob_fee(0)
