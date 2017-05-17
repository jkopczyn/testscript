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
    b2 = Duplicate.duplicate(board)
    b2.each_with_index do |row, y_idx|
        row.each_with_index do |cell, x_idx|
            next unless cell == MINE
            neighbors = neighbors([x_idx, y_idx], row.length, b2.length)
            neighbors.each do |x, y|
                if b2[y][x] == EMPTY
                    b2[y][x] = 1
                elsif b2[y][x].is_a? Integer
                    b2[y][x] += 1
                end
            end
        end
    end
end

def neighbors(cell_coordinates, board_length, board_width)
    [[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1,1]].map do |pair|
        [pair[0]+cell_coordinates[0], pair[1]+cell_coordinates[1]]
    end.select do |x, y|
        not (x < 0 or y < 0 or y >= board_width or x >= board_length)
    end
end

# If EMPTY -> expose neighbors, repeats
# If MINE -> die
# If NUMBER -> expose

def click_cell(board, click_coordinates)
    cell_value = board[click_coordinates[0]][click_coordinates[1]]
    if cell_value == MINE
        print "YOU DIED!"
        return false
    elsif cell_value == EMPTY
        board[click_coordinates[0]][click_coordinates[1]] = 0
        neighbors(click_coordinates, board[0].length, board.length).each do |new_coords|
            click_cell(board, new_coords)
        end
    end
    return board
end
