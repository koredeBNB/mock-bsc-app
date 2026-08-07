from __future__ import annotations


def get_gas_fee_status(network: str) -> dict[str, object]:
    """Return current gas fee information for documentation update demos."""
    return {
        "network": network,
        "base_fee_gwei": 3.5,
        "priority_fee_gwei": 1.1,
        "estimated_total_fee_gwei": 4.6,
        "blob_base_fee_gwei": 0.25,
        "max_fee_per_gas_gwei": 8.0,
        "congestion_level": "medium",
        "sample_block": 39126000,
        "fee_trend": "rising",
    }


def estimate_blob_fee(blob_count: int, network: str = "bnb-smart-chain") -> dict[str, object]:
    """Estimate total blob data-availability fee for a batch of blobs.

    Introduced for the full docs-automation E2E: source merge should drive
    MkDocs updates plus secondary AI review and LLMS.txt sync.
    """
    if blob_count < 1:
        raise ValueError("blob_count must be >= 1")
    status = get_gas_fee_status(network)
    per_blob = float(status["blob_base_fee_gwei"])
    return {
        "network": network,
        "blob_count": blob_count,
        "blob_base_fee_gwei": per_blob,
        "estimated_blob_fee_gwei": round(per_blob * blob_count, 4),
        "sample_block": status["sample_block"],
    }
