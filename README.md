# Sidorenko's Conjecture Counterexample Search

This project implements a numerical search for a counterexample to a specific case of **Sidorenko's Conjecture** related to the graph **`K₅,₅ \ C₁₀`** (the complete bipartite graph on 5+5 vertices minus a 10-cycle).

The search uses an **Adaptive Monte Carlo Search (AMCS)** algorithm to explore the space of matrices, guided by an **eigenvalue-based formulation** of the conjecture.

---

## 📐 The Mathematical Problem

[Sidorenko's conjecture](https://en.wikipedia.org/wiki/Sidorenko%27s_conjecture) is a major unsolved problem in graph theory. This project tests an equivalent formulation of the conjecture developed by **László Lovász**, which recasts the problem into linear algebra.

The core idea is to find an `m × n` matrix `M` with **non-negative entries** that could potentially violate the conjecture.

### ➤ Conjecture Test Procedure:

1. Construct a large `mn × mn` matrix `M_tilde` from `M`.
2. Calculate the eigenvalues `λ` of `M_tilde`.
3. Evaluate the inequality:

```math
\sum \lambda^5 \geq \frac{\left(\sum M\right)^{15}}{(mn)^{10}}
```

### 🔎 Conjecture Gap

The algorithm computes the **Gap** as:

```math
\text{Gap} = \sum \lambda^5 - \frac{\left(\sum M\right)^{15}}{(mn)^{10}}
```

- The **conjecture holds** if this `Gap ≥ 0`.
- The program **searches** for a matrix `M` that makes this gap **positive**, which would imply a **numerical counterexample**.

---

## 🧪 The Search Algorithm

To explore the high-dimensional space of possible matrices `M`, this project uses an **Adaptive Monte Carlo Search (AMCS)** strategy.

### 🔁 AMCS (Outer Loop)

The `AMCS_M` function in `amcs_eigenvalue.py` serves as the **search controller**:
- Dynamically adjusts **search intensity** based on recent progress.
- Iteratively improves the matrix `M` by invoking deeper local searches.

### 🔍 NMCS (Inner Loop)

The `NMCS_M` function performs a **nested Monte Carlo search**:
- Applies **random perturbations** to matrix `M`.
- Selects the best variant from each mutation round.

### 🎲 Perturbation Function

Defined in `helpers.py` as `perturb_M`, it:
- Randomly increases one matrix entry.
- Decreases another entry to keep matrix "mass" in balance.
- Produces a small, local "move" in matrix space.

### 🧮 Score Function

The search seeks to **maximize the score**, defined as:

```python
score = -Gap
```

- Maximizing the score = Minimizing the Gap
- A **positive Gap** indicates a potential violation of the conjecture.

---

## ⚙️ Prerequisites

Install the required libraries via pip:

```bash
pip install numpy numba
```

- `numpy`: Efficient numerical operations.
- `numba`: Just-in-time (JIT) compilation to accelerate loops.

---

## 🚀 How to Run

From the project directory, run the main script:

```bash
python main.py
```

---

## 📁 File Structure

```text
project/
│
├── main.py              # Main entry point for the search
├── helpers.py           # Mathematical utilities (matrix perturbation, M_tilde construction, etc.)
└── amcs_eigenvalue.py   # Core implementation of AMCS and NMCS algorithms
```

---

## 🛠️ Customization

Modify parameters in `main.py` to tailor the search:

- **Matrix Dimensions**  
  ```python
  m, n = 10, 10
  ```

- **Initial Matrix**  
  Use a specific seed instead of random initialization:
  ```python
  initial_M = np.ones((m, n))  # or any custom structured matrix
  ```

- **Search Intensity**  
  Change the depth and breadth of the search:
  ```python
  AMCS_M(initial_M, max_depth=100, max_level=5)
  ```

---

## 📌 Notes

- This project searches for **numerical counterexamples**, not symbolic ones.
- Precision issues may arise; numerical findings should be validated further.
- Parallelization or GPU-acceleration could improve performance for large `m × n`.
