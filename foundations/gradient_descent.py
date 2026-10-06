class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for _ in range(iterations):
            dx = 2 *x
            x = x - learning_rate * dx

        return round(x, 5)
            
