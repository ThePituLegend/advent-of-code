use std::fs;

fn parse_file(file_path: &str) -> Vec<Vec<char>> {
    fs::read_to_string(file_path)
        .expect("Failed to read the file")
        .lines() // split the string into an iterator of string slices
        .map(|l| l.chars().collect()) // make each slice into a string
        .collect() // gather them together into a vector
}

fn get_char(input: &[Vec<char>], r: i32, c: i32) -> char {
    *input
        .get(r as usize)
        .and_then(|row| row.get(c as usize))
        .unwrap_or(&' ')
}

fn check_xmas(input: &[Vec<char>], r: i32, c: i32) -> u32 {
    const XMAS: [char; 4] = ['X', 'M', 'A', 'S'];
    const DIRECTIONS: [(i32, i32); 8] = [
        (1, 0),   // Down
        (-1, 0),  // Up
        (0, 1),   // Right
        (0, -1),  // Left
        (1, 1),   // Down-Right
        (-1, 1),  // Up-Right
        (1, -1),  // Down-Left
        (-1, -1), // Up-Left
    ];

    DIRECTIONS
        .iter()
        .filter(|&&(dr, dc)| {
            (0..4).all(|i| get_char(input, r + i * dr, c + i * dc) == XMAS[i as usize])
        })
        .count()
        .try_into()
        .unwrap()
}

fn check_x_mas(input: &[Vec<char>], r: i32, c: i32) -> u32 {
    let r = r + 1;
    let c = c + 1; // Move to middle
    const X_MAS: [char; 3] = ['M', 'A', 'S'];
    const DIRECTIONS: [(i32, i32); 4] = [
        (1, 1),   // Down-Right
        (-1, 1),  // Up-Right
        (1, -1),  // Down-Left
        (-1, -1), // Up-Left
    ];

    (DIRECTIONS
        .iter()
        .filter(|&(dr, dc)| {
            (-1..=1).all(|i| get_char(input, r + i * dr, c + i * dc) == X_MAS[(i + 1) as usize])
        })
        .count()
        == 2) as u32
}

fn part(n: u8, input: &[Vec<char>], check: fn(&[Vec<char>], i32, i32) -> u32) {
    let result: u32 = input.iter().zip(0..).fold(0, |acc, (row, r)| {
        row.iter()
            .zip(0..)
            .fold(0, |acc_in, (_, c)| acc_in + check(input, r, c))
            + acc
    });

    println!("Result (Part {n}): {result}");
}

fn main() {
    println!("*** DAY 4 ***");

    let file_path = "input.txt";
    let input = parse_file(file_path);

    part(1, &input, check_xmas);
    part(2, &input, check_x_mas);
}
