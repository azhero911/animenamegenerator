#!/usr/bin/env bash
# wire-domain.sh
# Usage: ./wire-domain.sh https://yourdomain.com

if [ -z "$1" ]; then
  echo "Usage: ./wire-domain.sh https://yourdomain.com"
  exit 1
fi

python3 scripts/wire_domain.py "$1" 2>/dev/null || python scripts/wire_domain.py "$1"
