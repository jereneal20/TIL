class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        new_asteroids = []
        for asteroid in asteroids:
            while len(new_asteroids) != 0 and new_asteroids[-1] > 0:
                if new_asteroids[-1] > 0 and asteroid > 0:
                    break
                if new_asteroids[-1] > -asteroid:
                    asteroid = 0
                    break
                if new_asteroids[-1] == -asteroid:
                    asteroid = 0
                    new_asteroids.pop()
                    break
                new_asteroids.pop()
            if asteroid != 0:
                new_asteroids.append(asteroid)

        return new_asteroids
