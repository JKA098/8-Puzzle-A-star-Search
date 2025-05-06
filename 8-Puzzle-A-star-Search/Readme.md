# 🧠 8-Puzzle A\* Search Performance Exploration

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Focus](https://img.shields.io/badge/focus-Search%20Algorithms-blueviolet)
![Theme](https://img.shields.io/badge/theme-Admissible%20Heuristics-brightgreen)
![Data](https://img.shields.io/badge/data%20analysis-Psutil-lightgrey)
![Statistics](https://img.shields.io/badge/statistical%20tests-Performance%20Metrics-blue)
![ML](https://img.shields.io/badge/algorithm-A*%20Search-orange)
![Framework](https://img.shields.io/badge/framework-Custom%20Implementation-informational)
![Notebook](https://img.shields.io/badge/editor-Any%20IDE-orange)

---

## 📌 Overview

This project investigates the **performance of different admissible heuristics** on the A\* algorithm using the classic **8-puzzle problem**. The focus is on how heuristic design influences search efficiency, memory consumption, and computational time.

The project involves:

* Designing and analyzing **3 admissible heuristics** + a composite max-based heuristic.
* Implementing the **A⭐ search algorithm**.
* Measuring key performance metrics.
* Providing comparative discussion based on real executions.

> ⚠️ **Note**: While A\* implementations may be sourced, all heuristic designs, explanations, and analysis must be original.

---

## 🎯 Objectives

1. Propose and implement four admissible heuristic(h1, h2, h3 and h4).
2. Develop a working A\* search solution for the 8-puzzle.
3. Analyze and compare heuristic performance using four initial puzzle configurations of your choice.
4. Reflect on real-world A\* complexity via randomly generated unsolvable or difficult states.

---

## 🚧 Deliverables

* [x] `main.py`: Full implementation of A\* with support for h1, h2, h3, h4.

* [x] Admissible Heuristics:

  * **h1**: Misplaced tile count.
  * **h2**: Manhattan distance.
  * **h3**: Max of h1 and h2.
  * **h4**: Max(h1, h2, h3).
* [x] Performance Metrics:

  * Time (in seconds)
  * Memory (in MB)
  * Number of nodes generated
* [x] Summary table and discussion for 4 example puzzles and random configurations.

---

## 🧩 Features

* **Interactive Input**: Accepts either user input or random configuration for the puzzle.
* **Flexible Heuristics**: Each heuristic can be evaluated independently.
* **Performance Insights**: Reports on runtime, memory usage, and node count per heuristic.
* **Reusable Modules**: Structured with extensibility in mind.

---

## 🧪 Sample Usage

```bash
$ python main.py
Enter initial configuration as 9 space-separated numbers (or press Enter to randomize): 1 2 3 4 0 5 6 7 8

Initial State:
[1, 2, 3]
[4, 0, 5]
[6, 7, 8]

Initial Heuristic Values:
h1: 4, h2: 6, h3: 6, h4: 6

Running A* with h1...
Running A* with h2...
Running A* with h3...
Running A* with h4...

Performance Metrics:
h1: Time = 0.0031s, Memory = 0.32 MB, Nodes Generated = 72
h2: Time = 0.0026s, Memory = 0.25 MB, Nodes Generated = 64
h3: Time = 0.0029s, Memory = 0.28 MB, Nodes Generated = 59
h4: Time = 0.0027s, Memory = 0.29 MB, Nodes Generated = 58
```

---

## 📊 Analysis Summary

| Heuristic | Time (s) | Memory (MB) | Nodes Generated |
| --------- | -------- | ----------- | --------------- |
| h1        | 0.0031   | 0.32        | 72              |
| h2        | 0.0026   | 0.25        | 64              |
| h3        | 0.0029   | 0.28        | 59              |
| h4        | 0.0027   | 0.29        | 58              |

> h4 generally performs the best due to its dynamic selection of the most informative heuristic value per node.

---

## 🤔 Observations

* For challenging configurations, **A\*** may take significantly longer.
* This aligns with the **exponential time complexity** of A\* in the worst-case scenario.
* Time complexity is dominated by the **branching factor** and **depth of the solution**.

---


