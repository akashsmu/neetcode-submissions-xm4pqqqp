class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        first = init
        for i in range(iterations):
            value = 2 * first
            first = first - (learning_rate * value)
        
        return round(first,5)