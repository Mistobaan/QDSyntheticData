#!/bin/sh
docker run --gpus all \
    --ipc=host \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -shm-size=2g \
    --net=host \
    -v $PWD:/workspace reward_model python server.py