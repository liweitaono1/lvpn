#!/usr/bin/env bash
celery  worker -A lvpn --detach  -l INFO -f logs/celery.log  -c 1 -O OPTIMIZATION
