# SLE-3: Architectural Design Using C4 Model

## Course

**02AML204 – Introduction to Artificial Intelligence**

## Project Title

**Maze Solving System – C4 Architectural Design**

## 1. Overview

This project presents the architectural design of a Maze Solving System using the **C4 Model**.

The system uses **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to find a path from a starting position to a goal position in a maze.

This SLE-3 continues the work completed in previous SLEs:

* **SLE-1:** Implemented the search/maze-solving code.
* **SLE-2:** Performed performance analysis and comparison of BFS and DFS.
* **SLE-3:** Designed the complete system architecture using all four levels of the C4 Model.

---

## 2. Objectives

* Understand software architecture using the C4 Model.
* Represent the Maze Solving System at four different levels.
* Show the relationship between users, system modules, components, and code.
* Connect the architecture with the BFS and DFS implementation from previous SLEs.
* Keep the architecture simple, clear, and easy to understand.

---

## 3. C4 Model

The C4 Model represents software architecture using four levels:

| Level | Name          | Description                                                   |
| ----- | ------------- | ------------------------------------------------------------- |
| 1     | **Context**   | Shows the system and its interaction with the user.           |
| 2     | **Container** | Shows the main building blocks of the system.                 |
| 3     | **Component** | Shows the smaller parts inside the Search Engine.             |
| 4     | **Code**      | Shows the main functions and data used in the implementation. |

---

## 4. Level 1 – Context Diagram

The Context Diagram shows the Maze Solving System as a single system and its interaction with the user.

The user provides the maze, start position, and goal position. The system processes the input and returns the solved path or search result.

**Diagram:**
`docs/level1_context.png`

---

## 5. Level 2 – Container Diagram

The system is divided into the following main containers:

* **Input Module** – Receives the maze, start position, and goal position.
* **Search Engine** – Performs BFS or DFS to find a path.
* **Memory / Visited Set** – Keeps track of already explored positions.
* **Path Reconstruction** – Builds the final path from start to goal.
* **Output Module** – Displays the solved path and result.

**Diagram:**
`docs/level2_container.png`

---

## 6. Level 3 – Component Diagram

The **Search Engine** is selected as the main container for component-level design.

Its main components are:

* **BFS Search** – Uses a queue to explore the maze.
* **DFS Search** – Uses a stack to explore possible paths.
* **Visited Set** – Prevents repeated exploration.
* **Goal Test** – Checks whether the goal has been reached.
* **Path Reconstruction** – Generates the final path.

**Diagram:**
`docs/level3_component.png`

---

## 7. Level 4 – Code Level Overview

The main programming elements used in the Maze Solving System are:

| Code Element             | Responsibility                                              |
| ------------------------ | ----------------------------------------------------------- |
| `MAZE`                   | Stores the maze structure.                                  |
| `START` / `GOAL`         | Define the starting and destination positions.              |
| `print_maze_with_path()` | Displays the maze and the resulting path.                   |
| `get_neighbors()`        | Finds valid neighboring positions.                          |
| `solve_bfs()`            | Solves the maze using BFS.                                  |
| `solve_dfs()`            | Solves the maze using DFS.                                  |
| `run_profiling()`        | Runs the algorithms repeatedly and measures execution time. |

---

## 8. Design Decisions

The system is divided into separate modules to make the architecture simple and easy to understand. BFS and DFS are kept as separate search components so their performance can be compared. A Visited Set is used to avoid exploring the same position repeatedly. Input, search, path generation, and output are separated for easier modification and testing.

---

## 9. Connection with Previous SLEs

### SLE-1 – Implementation

The basic Maze Solving System and search algorithms were implemented.

### SLE-2 – Performance Analysis

BFS and DFS were executed repeatedly and their execution time and nodes expanded were compared.

### SLE-3 – Architecture

The same Maze Solving System is represented using all four levels of the C4 Model.

**Overall flow:**

`SLE-1 → Code → SLE-2 → Performance → SLE-3 → Architecture`

---

## 10. AI Contribution

**AI Tool Used:** ChatGPT

AI was used to understand the C4 Model, organize the architecture into four levels, and improve the clarity of the documentation.

The implementation, testing, performance analysis, architecture verification, and final diagrams were completed and reviewed by the student.

---

## 11. Conclusion

The C4 Model helped in understanding the architecture of the Maze Solving System at different levels. It shows how the system moves from a high-level user interaction to containers, components, and actual code functions. The architecture makes the system easier to understand, modify, test, and compare.

---

## 12. Repository Structure

```text
SLE-3/
│
├── README.md
├── Contribution_Log.md
│
├── code/
│   └── maze_solver.py
│
└── docs/
    ├── level1_context.png
    ├── level2_container.png
    └── level3_component.png
```
