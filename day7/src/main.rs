use std::fs;

fn parse_file(file_path: &str) -> Vec<(u64, Vec<u64>)> {
    fs::read_to_string(file_path)
        .expect("Failed to read the file")
        .lines()
        .map(|line| {
            let mut parts = line.split(':');
            let test_val = parts.next().unwrap().trim().parse().unwrap();
            let equation = parts
                .next()
                .unwrap()
                .split_whitespace()
                .filter_map(|v| v.parse().ok())
                .collect();
            (test_val, equation)
        })
        .collect()
}

fn check_equation_two(test_val: u64, equation: &[u64]) -> bool {
    let n = equation.len() - 1;

    // Iterate over 2^n possibilities
    (0..(1 << n)).any(|mask| {
        (0..n).fold(equation[0], |acc, i| {
            if (mask & (1 << i)) != 0 {
                // If "bit" is 1, multiply
                acc * equation[i + 1]
            } else {
                // Else, sum
                acc + equation[i + 1]
            }
        }) == test_val
    })
}

fn check_equation_three(test_val: u64, equation: &[u64]) -> bool {
    let n = equation.len() - 1;

    // Iterate over 3^n possibilities
    (0..(3_u64.pow(n as u32))).any(|mask| {
        (0..n).fold(equation[0], |acc, i| {
            match (mask / 3_u64.pow(i as u32)) % 3 {
                0 => acc + equation[i + 1],
                1 => acc * equation[i + 1],
                2 => format!("{}{}", acc, equation[i + 1]).parse().unwrap(),
                _ => acc, // Default case
            }
        }) == test_val
    })
}

fn part(n: u32, calibrations: &[(u64, Vec<u64>)], checker: fn(u64, &[u64]) -> bool) {
    let result: u64 = calibrations
        .iter()
        .filter_map(|(test_val, equation)| {
            if checker(*test_val, equation) {
                Some(*test_val)
            } else {
                None
            }
        })
        .sum();

    println!("Result (Part {n}): {result}");
}

fn main() {
    println!("*** DAY 7 ***");

    let file_path = "input.txt";
    let calibrations = parse_file(file_path);

    part(1, &calibrations, check_equation_two);
    part(2, &calibrations, check_equation_three);
}
