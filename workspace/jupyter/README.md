# Jupyter Notebook server

Setup a jupyter server inside the docker compose workspace. Allows to interact seamleassly with the other services


## Debug Notebook

```bash
docker build . -t notebook
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    -p 8888 \
    -v $HOME/workspace/QDSyntheticData/:/workspace notebook start-notebook.py 
```