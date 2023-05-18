## Overview
Repo to build docker image to run Vall-e python.

### How To Clone

```
git clone --recurse-submodules <address.git>
```

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

### Run and Mount Data Folder on Container for Training 
```
 docker run --gpus all --volume ${pwd}/data:/data  vall-e 
```

### Test Torch GPU 
```
 docker run --gpus all  vall-e "python" "test.py"
```
or
```
 docker run --gpus all  vall-e nvidia-smi  
```
 

### NEW COMMAND
In WSL Terminal in vale repo run   
```
docker run  --gpus all --volume $(pwd)/data:/code/data -it  vall-e
```