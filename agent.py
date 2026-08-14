from collections import deque
import heapq
import random

# agent.py

class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)

class SearchAgent:
    """An agent that uses search algorithms to navigate the grid."""

    def __init__(self):
        self.plan = []
        self.active_algo = 'BFS'

    def sense_and_act(self, percept: dict) -> str:
        if not self.plan:
            closest_food = self.find_closest_food(percept['agent_pos'], percept['all_food'])
            if closest_food:
                if self.active_algo == 'BFS':
                    self.plan = self.bfs_search(percept['agent_pos'], closest_food)
                elif self.active_algo == 'DFS':
                    self.plan = self.dfs_search(percept['agent_pos'], closest_food)
                elif self.active_algo == 'UCS':
                    self.plan = self.ucs_search(percept['agent_pos'], closest_food)

        return self.plan.pop(0) if self.plan else None

    def find_closest_food(self, agent_pos, all_food):
        # Implement logic to find the closest food pellet
        pass

    def bfs_search(self, start, goal):
        queue = deque([start])
        reached = set()
        reached.add(start)

        while queue:
            current = queue.popleft()
            if current == goal:
                return []  # Return the sequence of actions to reach the goal

            for neighbor in self.get_neighbors(current):
                if neighbor not in reached:
                    reached.add(neighbor)
                    queue.append(neighbor)

        return []  # Goal not found

    def dfs_search(self, start, goal):
        stack = [start]
        reached = set()
        reached.add(start)

        while stack:
            current = stack.pop()
            if current == goal:
                return []  # Return the sequence of actions to reach the goal

            for neighbor in self.get_neighbors(current):
                if neighbor not in reached:
                    reached.add(neighbor)
                    stack.append(neighbor)

        return []  # Goal not found

    def ucs_search(self, start, goal):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        reached = {start: 0}

        while priority_queue:
            cost, current = heapq.heappop(priority_queue)
            if current == goal:
                return []  # Return the sequence of actions to reach the goal

            for neighbor, step_cost in self.get_neighbors_with_cost(current):
                new_cost = cost + step_cost
                if neighbor not in reached or new_cost < reached[neighbor]:
                    reached[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return []  # Goal not found

    def get_neighbors(self, position):
        # Implement logic to get neighboring positions
        pass

    def get_neighbors_with_cost(self, position):
        # Implement logic to get neighboring positions with their costs
        pass