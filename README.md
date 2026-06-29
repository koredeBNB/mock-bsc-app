# Mock BSC App

Small mock source repository used to test the AI docsite update GitHub App.

This repo stands in for a BNB Chain source repository. When a pull request is merged into `main`, the GitHub App should inspect the code diff and update the separate MkDocs docsite repository if the documented API behavior changed.

## Validator API

The demo API exposes validator status:

```python
from mock_bsc_app.validators import get_validator_status

status = get_validator_status("validator-1")
```

The response includes:

- `validator_id`
- `status`
- `commission_rate`

Future demo changes can add or rename response fields to trigger an AI-generated documentation update.

## Development

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
```
