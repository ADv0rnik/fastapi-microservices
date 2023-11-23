#!/bin/bash

# shellcheck disable=SC2164
cd .. && alembic upgrade head

python main.py