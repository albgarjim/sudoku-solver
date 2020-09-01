# Sudoku solver


[//]: # "References"
[contact-albert]: albgarjim1@gmail.com
[kaggle-sudoku-dataset]: https://www.kaggle.com/bryanpark/sudoku

Algorithm to solve sudokus
<!-- description of what the project does  -->

## Table of Contents

- [Project title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Results](#results)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Contact](#contact)

## Introduction

The following algorithm solves sudokus using a recursive brute force method and also incorporates a human solvable method that aims to solve the sudoku like a person would.

## Results

Receives a sudoku as a string of numbers, example:

```
'003800510008700930100305728000200849801906257000500163964127385382659471010400692'
```

The numbers marked as `0` are the empty cells

After processing any of the two methods returns `True` if the sudoku is solvable together with the solution in the shape of a matrix

## Installation


Clone this repository with the command:

```sh
git clone https://github.com/albgarjim/sudoku-solver.git
```

Navigate into the src file insidie the `sudoku-solver` folder:

```sh
cd ./src/sudoku-solver
```

This project requires the following python libraries:
- csv

<!-- name technologies used and how to build project -->


## Usage

This project has been tested using the [kaggle sudoku dataset][kaggle-sudoku-dataset]. In order to use it, download the dataset and specify the path in the `dataset` variable on `solver.py`. Example:

```
dataset = "$HOME/Documents/sudoku-solver/sudoku-dataset/sudoku.csv"
```

After importing the dataset or declaring a sudoku as a string of numbers, like in [Results](#results), call the function `create_sudoku_matrix` which accepts said string. Once the matrix is created, it can be passed to `bruteforce` or `human_solvable` functions declared on `lib_sudoku_solver.py`


## License

Released under MIT license



## Contact

Maintainer: [Alberto Garcia][contact-alberto]
