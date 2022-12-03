use std::fs;

const DRAW_SCORE: i32 = 3;
const WIN_SCORE: i32 = 6;
const WINNING_RULES: [(i32, i32); 3] = [(1, 3), (3, 2), (2, 1)]; // x wins agains y

fn sum_game_score(str_input: &str) -> i32 {
    str_input.lines().map(calc_result_round).sum()
}

fn sum_game_indicated(str_input: &str) -> i32 {
    str_input.lines().map(calc_indicated_round).sum()
}

fn calc_result_round(str_input: &str) -> i32 {
    let my_shape = determine_points_for_my_shape(str_input);
    let opponent_shape = determine_points_for_opponent_shape(str_input);
    my_shape + determine_points_for_result(my_shape, opponent_shape)
}

fn calc_indicated_round(str_input: &str) -> i32 {
    let opponent_shape = determine_points_for_opponent_shape(str_input);
    let result = match get_nth_char(str_input, 2) {
        'X' => 0,
        'Y' => DRAW_SCORE,
        'Z' => WIN_SCORE,
        _ => 0,
    };
    let my_shape = if result == DRAW_SCORE {
        opponent_shape
    } else {
        match (result, opponent_shape) {
            (0, 1) => 3,
            (0, 3) => 2,
            (0, 2) => 1,
            (6, 3) => 1,
            (6, 2) => 3,
            (6, 1) => 2,
            _ => 0,
        }
    };
    my_shape + determine_points_for_result(my_shape, opponent_shape)
}

fn determine_points_for_result(my_shape: i32, opponent_shape: i32) -> i32 {
    if my_shape == opponent_shape {
        return DRAW_SCORE;
    }
    if WINNING_RULES.contains(&(my_shape, opponent_shape)) {
        return WIN_SCORE;
    };
    0
}

fn determine_points_for_my_shape(str_input: &str) -> i32 {
    shape2points(get_nth_char(str_input, 2))
}

fn determine_points_for_opponent_shape(str_input: &str) -> i32 {
    shape2points(get_nth_char(str_input, 0))
}

fn shape2points(shape: char) -> i32 {
    match shape {
        'X' | 'A' => 1,
        'Y' | 'B' => 2,
        'Z' | 'C' => 3,
        _ => 0,
    }
}

fn get_nth_char(str_input: &str, n: usize) -> char {
    str_input.chars().nth(n).unwrap()
}

fn main() {
    let contents = fs::read_to_string("../day2-input.txt").expect("data file not found");
    println!("sum_game_score: {}", sum_game_score(&contents));
    println!("sum_game_indicated: {}", sum_game_indicated(&contents));
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "\
A Y
B X
C Z
";

    #[test]
    fn test_part_a() {
        assert_eq!(sum_game_score(TEST_INPUT), 15);
    }

    #[test]
    fn test_part_b() {
        assert_eq!(sum_game_indicated(TEST_INPUT), 12);
    }
}
