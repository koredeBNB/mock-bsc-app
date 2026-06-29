from __future__ import annotations


def get_validator_status(validator_id: str) -> dict[str, object]:
    """Return a small validator status payload for documentation update demos."""
    return {
        "validator_id": validator_id,
        "status": "active",
        "commission_rate": 0.05,
    }
