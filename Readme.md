## Overview
Repo to build docker image to run Vall-e python.

### How To Build
```
docker build -t vall-e -f DockerFile .
```

### How To Run
```
 docker run --gpus all  vall-e
```

### Run with CMD ARGS
```
docker run --gpus all  vall-e "python" "-m" "vall_e.emb.g2p" "data/test"
```

### Test Torch GPU 
```
 docker run --gpus all  vall-e "python" "test.py"
```
or
```
 docker run --gpus all  vall-e nvidia-smi  
```