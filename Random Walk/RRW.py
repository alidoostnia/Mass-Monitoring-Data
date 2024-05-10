import random
import math

def reinforced_random_walk(reward_structure, lam):
    # Initialize variables
    X_n = 0  # Walker's initial position
    observed_rewards = {i: 0 for i in reward_structure.keys()}  # Observed rewards
    expected_rewards = {i: 0 for i in reward_structure.keys()}  # Expected rewards
    probabilities = {i: 1 / len(reward_structure) for i in reward_structure.keys()}  # Probabilities

    # Main loop
    while True:
        # Observe current position and available directions
        current_position = X_n
        available_directions = reward_structure.keys()

        # Update observed and expected rewards, and probabilities for each direction
        for direction in available_directions:
            observed_rewards[direction] += reward_structure[direction][current_position]
            expected_rewards[direction] = observed_rewards[direction] / (current_position + 1)
            probabilities[direction] = math.exp(lam * expected_rewards[direction])

        # Choose direction to move based on probabilities
        move_direction = random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0]

        # Update walker's position
        X_n += move_direction

        # Check termination condition
        if termination_condition_met():
            break

    return X_n

def termination_condition_met():
    # Implement your termination condition logic here
    # For example, you can check if a certain number of steps has been reached
    pass

# Example usage
reward_structure = {
    0: [1, 2, 3],
    1: [2, 3, 4],
    2: [3, 4, 5]
}
lam = 0.5
random_walk_path = reinforced_random_walk(reward_structure, lam)
print(random_walk_path)