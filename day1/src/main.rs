use std::fs;

fn elves_calories(str_input: &str) -> Vec<i32> {
    let mut output: Vec<i32> = str_input.lines().fold(Vec::new(), |mut acc, x| {
        if x.is_empty() || acc.is_empty() {
            acc.push(0);
        } else {
            let n = acc.len() - 1;
            acc[n] += x.parse::<i32>().unwrap();
        }
        acc
    });
    output.sort();
    output.reverse();
    output
}

fn calories_of_elf_with_most_energy(str_input: &str) -> i32 {
    elves_calories(str_input)[0]
}

fn calories_of_top_three_elves(str_input: &str) -> i32 {
    elves_calories(str_input)[0..3].iter().sum()
}

fn main() {
    let contents = fs::read_to_string("../day1-input.txt").expect("data file not found");

    println!(
        "calories_of_elf_with_most_energy: {}",
        calories_of_elf_with_most_energy(&contents)
    );
    println!(
        "calories_of_top_three_elves: {}",
        calories_of_top_three_elves(&contents)
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    fn test_part_a() {
        assert_eq!(calories_of_elf_with_most_energy(TEST_INPUT), 24000);
    }

    #[test]
    fn test_part_b() {
        assert_eq!(calories_of_top_three_elves(TEST_INPUT), 45000);
    }
}
