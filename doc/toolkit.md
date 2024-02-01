[![Build](https://github.com/wildmeshing/wildmeshing-toolkit/actions/workflows/continuous.yml/badge.svg)](https://github.com/wildmeshing/wildmeshing-toolkit/actions/workflows/continuous.yml)
[![codecov](https://codecov.io/github/wildmeshing/wildmeshing-toolkit/graph/badge.svg?token=CSBKSLUQW6)](https://codecov.io/github/wildmeshing/wildmeshing-toolkit)

# Wildmeshing-toolkit: Declarative Specification for Unstructured Mesh Editing Algorithms


This repository has gone through substantial changes that diverge from the API described by the SIGGRAPH Asia 2022 paper.
This prior version can be accessed [here](wildmeshing-toolkit/tree/1.0) as tag 1.0.

## Installation

#### via CMake

- Clone the repository into your local machine:

```bash
git clone https://github.com/wildmeshing/wildmeshing-toolkit.git
```

- Compile the code using cmake>3.20.0

```bash
cd wildmeshing-toolkit
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
```

You may need to install `gmp` before compiling the code. You can install `gmp` via [homebrew](https://brew.sh/).

Perl ([Windows link](https://strawberryperl.com/)) needs to be installed before running `cmake`. This is a requirement from `hdf5`.

## Usage
To reproduce figures from the paper, please use the commands from [reproduce_scripts](reproduce_scripts.sh). Note that the input data are from `wmtk-data-package.zip`. (Download: https://drive.google.com/drive/folders/1jFdQ77E2_n3EJF5_bPOOMEOxF4dyctjN?usp=sharing)


## About Us
This toolkit is a novel approach to describe mesh generation, mesh adaptation, and geometric modeling algorithms relying on changing mesh connectivity using a high-level abstraction. The main motivation is to enable easy customization and development of these algorithms via a declarative specification consisting of a set of per-element invariants, operation scheduling,and attribute transfer for each editing operation.

Many widely used algorithms editing surfaces and volumes
can be compactly expressed with our abstraction, and their implementation
within our framework is simple, automatically parallelizable on shared-
memory architectures, and with guaranteed satisfaction of the prescribed
invariants. These algorithms are readable and easy to customize for specific use cases.

This software library implements the abstractiona in our paper and providing automatic shared memory parallelization.

We will use the implementation of the shortest edge collapse algorithm as an example to introduce the framework and run through the basic software structures and APIs of the toolkit. All the code that is referenced below can be found under the `app` folder of the toolkit.
