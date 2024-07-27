# LeetCode Solutions in Python

Welcome to the repository of LeetCode solutions in Python. This repository aims to help you practice and improve your problem-solving skills with Python by solving a variety of problems available on [LeetCode](https://leetcode.com/).

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Solution Structure](#solution-structure)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains solutions to problems from LeetCode, implemented in Python. Each solution is accompanied by a detailed explanation and test cases to ensure correctness and understanding.

## Setup

To get started with the repository, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Termication/Leetcode-Python.git
    cd Leetcode-Python
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. **Navigate to the problem directory**: Each problem is stored in its own directory within the `problems` folder.
    ```bash
    cd problems/two-sum
    ```

2. **Run the solution**: You can run the solution script directly.
    ```bash
    python solution.py
    ```

3. **Run tests**: Each problem includes a test file to verify the solution.
    ```bash
    python test_solution.py
    ```

## Solution Structure

Each problem directory typically contains the following files:

- `README.md`: Description of the problem and the solution approach.
- `solution.py`: Python implementation of the solution.
- `test_solution.py`: Test cases to verify the solution.

## Example

Here's a simple example to illustrate the structure:

### Problem: Two Sum

#### Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

#### Solution Approach

We use a hash map to store the indices of the elements as we iterate through the array. For each element, we check if its complement (i.e., `target - element`) is already in the hash map.

#### File Structure

problems/
└── two-sum/
├── README.md
├── solution.py
└── test_solution.py

python


#### solution.py

```python
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]
```

### test_solution.py

```python

import unittest
from solution import two_sum

class TestTwoSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
    def test_no_solution(self):
        self.assertIsNone(two_sum([1, 2, 3], 7))

if __name__ == "__main__":
    unittest.main()
```
# Contributing

Contributions are welcome! If you have a new solution or an improvement to an existing solution, feel free to create a pull request.
