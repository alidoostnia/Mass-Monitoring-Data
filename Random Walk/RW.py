import random

def generate_random_walk(security_signal):
    # Initialize variables
    current_location = (0, 0)  # Start at origin (0, 0)
    visited_locations = set()
    walk = [current_location]  # Store the walk as a list of locations

    # Define movement directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # Function to check if a move is valid (not visited before)
    def is_valid_move(location, direction):
        new_location = (location[0] + direction[0], location[1] + direction[1])
        return new_location not in visited_locations

    # Generate random walk until all directions are blocked
    while any(is_valid_move(current_location, d) for d in directions):
        valid_directions = [d for d in directions if is_valid_move(current_location, d)]
        move_direction = random.choice(valid_directions)  # Choose a random valid direction
        current_location = (current_location[0] + move_direction[0], current_location[1] + move_direction[1])
        visited_locations.add(current_location)
        walk.append(current_location)

    return walk

# Example usage:
security_signal = {
    "Timestamp": "2024-03-21T10:15:28",
    "EventID": "FWL-20240321101528",
    "SourceIP": "192.168.1.10",
    "DestinationIP": "54.239.26.214",
    "SourcePort": 53748,
    "DestinationPort": 443,
    "Protocol": "TCP",
    "EventDescription": "Connection allowed from internal host to external IP address over HTTPS.",
    "Severity": "Medium",
    "Category": "Network Traffic",
    "AlertID": None,
    "UserID": None,
    "Hostname": "Firewall-1",
    "EventDetails": "The outbound HTTPS connection was permitted by the firewall rule named 'Outbound-HTTPS'."
}

random_walk = generate_random_walk(security_signal)
print(random_walk)
