param(
    [Parameter(Mandatory=$true)]
    [string]$Task
)

switch ($Task) {
    "test" {
        python -m pytest tests/
    }

    "trace" {
        python -m pytest tests/ --tracing=retain-on-failure --output=test-results
    }

    "headed" {
        python -m pytest tests/ --headed
    }

    "repeat10" {
        python -m pytest tests/ --count=10
    }

    "failed" {
        python -m pytest --lf
    }

    "lint" {
        python -m ruff check src config conftest.py
        if ($?) {
            python -m ruff check tests --select E501
        }
    }

    "show-trace" {
       playwright show-trace test-results\...\trace.zip
    }

    default {
        Write-Host "Unknown task: $Task"
        Write-Host "Available: test, trace, headed, repeat10, failed, lint"
    }
}