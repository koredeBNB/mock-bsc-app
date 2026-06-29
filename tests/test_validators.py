from __future__ import annotations

from mock_bsc_app.validators import get_validator_status


def test_get_validator_status_returns_documented_fields() -> None:
    status = get_validator_status("validator-1")

    assert status == {
        "validator_id": "validator-1",
        "status": "active",
        "commission_rate": 0.05,
        "voting_power": 1000,
        "delegator_count": 25,
        "uptime_percent": 99.9,
        "jailed_bnb": False,
    }
