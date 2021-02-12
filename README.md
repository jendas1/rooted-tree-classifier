
## Description

This folder contains a program that decides round complexity of homogenous LCL problems on (binary) trees.

The program uses three subroutines to determines a problem's complexity.

- constant_decider
    - decides whether a problem is O(1) solvable or it is inherently harder
- log_decider
    - decides whether a problem is log(n) solvable or it is inherently harder
- log_star_decider
    - decides whether a problem is log*(n) solvable or it is inherently harder

## Usage

1. Install dependencies by `pip3 install -r requirements.txt`.

2. Run `python -m rooted_tree_classifier` and describe (on standard input) constraints of a problem.
For example:

_Note that one needs to first run the classifier (`python -m rooted_tree_classifier`) and only afterwards provide an input
on a separate line._

```
python -m rooted_tree_classifier
111
```
Expected output is `O(1)`

```
python -m rooted_tree_classifier
112 121 122
```
Expected output is `O(1)`

```
python -m rooted_tree_classifier
121 131 212 323
```
Expected output is `O(log*n)`

```
python -m rooted_tree_classifier
112 121
```
Expected output is `Θ(log n)`

```
python -m rooted_tree_classifier
112 123 131
```
Expected output is `Θ(log n)`

```
python -m rooted_tree_classifier
121 212
```
Expected output is `Ω(n)`
## Tests

To execute tests, run the following from the root directory:

```
python -m unittest discover
```
