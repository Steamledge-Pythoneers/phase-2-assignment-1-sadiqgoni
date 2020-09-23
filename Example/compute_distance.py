def distance_to_destination(current_pos, target_pos):
    """"Returns the distance to destination.
    
    current_pos (int) - current position in integer
    target_pos (int)  - target position in integer
    """
    return [0 if target_pos - current_pos < 0 else target_pos - current_pos][0]
