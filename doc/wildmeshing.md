[![Build](https://github.com/wildmeshing/wildmeshing-toolkit/actions/workflows/continuous.yml/badge.svg)](https://github.com/wildmeshing/wildmeshing-toolkit/actions/workflows/continuous.yml)
[![codecov](https://codecov.io/github/wildmeshing/wildmeshing-toolkit/graph/badge.svg?token=CSBKSLUQW6)](https://codecov.io/github/wildmeshing/wildmeshing-toolkit)

# Wildmeshing-toolkit: Declarative Specification for Unstructured Mesh Editing Algorithms

This repository has gone through substantial changes that diverge from the API described by the SIGGRAPH Asia 2022 paper.
This prior version can be accessed [here](https://github.com/wildmeshing/wildmeshing-toolkit/releases/tag/1.0) as tag 1.0.

## Installation and Usage

Details on how to install and use the toolkit can be found in the [toolkit documentation](https://wildmeshing.github.io/wildmeshing-toolkit/index.html) or the [repository](https://github.com/wildmeshing/wildmeshing-toolkit/).

## About Us

This toolkit is a novel approach to describe mesh generation, mesh adaptation, and geometric modeling algorithms relying on changing mesh connectivity using a high-level abstraction. The main motivation is to enable easy customization and development of these algorithms via a declarative specification consisting of a set of per-element invariants, operation scheduling,and attribute transfer for each editing operation.

Many widely used algorithms editing surfaces and volumes
can be compactly expressed with our abstraction, and their implementation
within our framework is simple, automatically parallelizable on shared-
memory architectures, and with guaranteed satisfaction of the prescribed
invariants. These algorithms are readable and easy to customize for specific use cases.

This software library implements the abstractiona in our paper and providing automatic shared memory parallelization.
