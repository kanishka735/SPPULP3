# Practical 4: Gradient Descent Optimization

## Objective
Implement the Gradient Descent optimization algorithm from scratch to find the local minimum of a mathematical function:
$$f(x) = x^2 + 4x + 5$$

---

## Theory & Mathematical Formulation
Gradient Descent is a first-order iterative optimization algorithm for finding the local minimum of a differentiable function.
- **Objective Function**: $f(x) = x^2 + 4x + 5$
- **Derivative (Gradient)**: $f'(x) = \frac{df}{dx} = 2x + 4$
- **Update Rule**:
  $$x_{\text{new}} = x_{\text{old}} - \eta \cdot f'(x_{\text{old}})$$
  where $\eta$ is the learning rate (step size).

### Analytical Minimum
Setting $f'(x) = 0 \implies 2x + 4 = 0 \implies x = -2$.
Minimum value: $f(-2) = (-2)^2 + 4(-2) + 5 = 4 - 8 + 5 = 1$.

---

## Files in this Directory
- `gradient_descent.py` / `04_gradient_descent_local_min.py`: Standalone Python implementation with iteration tracking and convergence reporting.
- `gradient_descent.ipynb` / `04_gradient_descent_local_minimum.ipynb`: Jupyter notebook version.

*(Note: This practical is analytical and optimization-based; no external CSV dataset is required).*

---

## How to Run

### Command Line
```bash
cd Group-B-Machine-Learning/04-Gradient-Descent
python gradient_descent.py
```

### Jupyter Notebook
```bash
jupyter notebook gradient_descent.ipynb
```
