# translation

[Change boot order](https://easylinuxtipsproject.blogspot.com/p/tips-1.html#ID1)

## Conda

[Miniconda command line install](https://docs.anaconda.com/free/miniconda/#quick-command-line-install).

## Set mamba as solver

[Set mamba as solver](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community)

```sh
conda update -n base conda
```

```sh
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

## CUDA

Check latest supported driver -> choose compatible cuda version

[List of CUDA versions and matching driver versions](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)

# CHECK PYTORCH CUDA VERSION AND DRIVER COMPATIBILITY

[CUDA Installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#)

[CUDA alternate link?](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local)

[Wikipedia CUDA Version for each GPU](https://en.wikipedia.org/wiki/CUDA)

[CUDA Versions download list](https://developer.nvidia.com/cuda-toolkit-archive)

- cuda dependencies
  - versions and links
- installation guide
  - including tests (running nvidia-smi)

## Repo setup (Stuff to only run once)

- intial setup guide
  - everything that has to be done once
  - conda env creation, dependency installation

### Setup conda environment

Run this command to create the virutual environment based on the configuration file `environment.yaml`.

```sh
conda env create -f environment.yaml
```

You should see the following output:

```sh
UPDATE OUTPUT XD
```

After this you can activate the environment at anytime using

```sh
conda activate translation
```

## How to use this repo for actual translation

- usage guide
  - notebook explanation
  - (terminal)

## Models

[mBART-50 many to many multilingual machine translation](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)
