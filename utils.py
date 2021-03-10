def parse_test_boards(filepath):
    with open(filepath, 'r') as f:
        sequences = f.read().split('\n')
    puzzles = []
    for seq in sequences:
        puzzle = [list(map(int, seq[i:i+9])) for i in range(0, len(seq), 9)]
        puzzles.append(puzzle)

    return puzzles
