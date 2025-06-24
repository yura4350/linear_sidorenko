import numpy as np
from time import time
from amcs_eigenvalue import AMCS_M

if __name__ == "__main__":
    # Define the dimensions of the matrix M to search over.
    # We can start with a simple 5x5 case.
    m, n = 10, 10
    
    # Define an initial random M with non-negative entries between 0 and 1.
    # A non-uniform start might be more interesting.
    initial_M = np.random.rand(m, n)
    
    print(f"--- Searching for counterexample to Sidorenko's Conjecture for K5,5 \\ C10 ---")
    print(f"--- Using eigenvalue formulation on {m}x{n} matrices ---")
    print("Initial M:")
    print(np.round(initial_M, 3))

    # --- Run the AMCS Optimization ---
    start_time = time()
    M_final, final_gap = AMCS_M(initial_M, max_depth=10, max_level=5)
    print(f"\nTotal search time: {time() - start_time:.2f} seconds")