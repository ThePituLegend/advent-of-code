use std::fs;

fn parse_file(file_path: &str) -> (Vec<i32>, Vec<i32>) {
    let contents = fs::read_to_string(file_path).expect("Failed to read the file");
    let (col1, col2): (Vec<i32>, Vec<i32>) = contents
        .lines()
        .map(|line| {
            let mut split = line.split_whitespace();
            (
                split.next().unwrap().parse::<i32>().unwrap(),
                split.next().unwrap().parse::<i32>().unwrap(),
            )
        })
        .unzip();
    (col1, col2)
}

fn part1(file_path: &str) {
    let (mut col1, mut col2) = parse_file(file_path);

    col1.sort();
    col2.sort();

    let result: i32 = col1
        .iter()
        .zip(col2.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();

    println!("Result (Part 1): {}", result);
}

fn part2(file_path: &str) {
    let (col1, col2) = parse_file(file_path);

    let result: i32 = col1
        .iter()
        .map(|a| a * col2.iter().filter(|&x| x == a).count() as i32)
        .sum();

    println!("Result (Part 2): {}", result);
}

fn main() {
    println!("*** DAY 1 ***");

    let file_path = "input.txt";

    part1(file_path);
    part2(file_path);
}
