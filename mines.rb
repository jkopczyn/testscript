require "duplicate"

MINE = "*"
EMPTY = " "

def new_minesweeper_game(length, width, mine_count)
    board = Array.new(length) { |k| Array.new(width) {|k| EMPTY} }
    locations = random_subset((length*width).times.to_a, mine_count)
    locations.each do |idx|
        x, y = idx / width, idx % width
        board[x][y] = MINE
    end
    board
end

def new_minesweeper_game_with_adjacencies(length, width, mine_count)
    board = Array.new(length) { |k| Array.new(width) {|k| EMPTY} }
    locations = random_subset((length*width).times.to_a, mine_count)
    locations.each do |idx|
        y, x = idx / width, idx % width
        board[y][x] = MINE
        increment_neighbors(board, [x,y])
    end
    board
end

def random_subset(list, select)
    new_list = list.dup
    list.length.times do |idx|
        tmp = rand(idx+1)
        new_list[idx] = new_list[tmp]
        new_list[tmp] = list[idx]
    end
    new_list[0...select]
end

#| 0 0 0 |
#| 1 1 1 |
#| 1 * 1 |
#| 1 1 1 |

def generate_adjacencies(board)
    b2 = duplicate(board)
    b2.each_with_index do |row, y_idx|
        row.each_with_index do |cell, x_idx|
            next unless cell == MINE
            increment_neighbors(b2, [x_idx, y_idx])
        end
    end
end

def increment_neighbors(board, cell_coords)
    neighbors = neighbors(
        [cell_coords[0], cell_coords[1]],
        board[0].length,
        board.length
    )
    neighbors.each do |x, y|
        if board[y][x] == EMPTY
            board[y][x] = 1
        elsif board[y][x].is_a? Integer
            board[y][x] += 1
        end
    end
end


KING_MOVES =[[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1,1]]

def neighbors(cell_coordinates, board_length, board_width)
    KING_MOVES.map do |pair|
        [pair[0]+cell_coordinates[0], pair[1]+cell_coordinates[1]]
    end.select do |x, y|
        not (x < 0 or y < 0 or y >= board_width or x >= board_length)
    end
end

# If EMPTY -> expose neighbors, repeats
# If MINE -> die
# If NUMBER -> expose

def click_cell(board, click_coordinates)
    if board[click_coordinates[1]][click_coordinates[0]] == MINE
        print "YOU DIED!"
        return false
    end
    new_board = duplicate(board)
    click_cell_mutator(new_board, click_coordinates)
    new_board
end

def click_cell_mutator(board, click_coordinates)
    if board[click_coordinates[1]][click_coordinates[0]] == EMPTY
        board[click_coordinates[1]][click_coordinates[0]] = 0
        neighbors(
            click_coordinates,
            board[0].length,
            board.length
        ).each { |new_coords|
            click_cell_mutator(board, new_coords) }
    end
end

b = new_minesweeper_game(9,12,10); b2 = generate_adjacencies(b)
c = new_minesweeper_game_with_adjacencies(9,12,10)
