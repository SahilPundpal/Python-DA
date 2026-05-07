def judgeCircle(moves: str) -> bool:
    """
    Check if robot returns to origin after executing all moves.
    
    Args:
        moves: String of moves ('U', 'D', 'L', 'R')
    
    Returns:
        True if robot ends at origin (0,0), False otherwise
    """
    # Track position
    x, y = 0, 0
    
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
    
    return x == 0 and y == 0


# Test cases
if __name__ == "__main__":
    # Example 1
    print(f"'UD' -> {judgeCircle('UD')}")  # Expected: True
    
    # Example 2
    print(f"'LL' -> {judgeCircle('LL')}")  # Expected: False
    
    # Additional tests
    print(f"'UDLR' -> {judgeCircle('UDLR')}")  # Expected: True
    print(f"'UUDDLLRR' -> {judgeCircle('UUDDLLRR')}")  # Expected: True
    print(f"'UUDDLLRRR' -> {judgeCircle('UUDDLLRRR')}")  # Expected: False
