use std::fs;

fn parse_file(file_path: &str) -> Vec<Vec<i32>> {
    let contents = fs::read_to_string(file_path).expect("Failed to read the file");
    let reports = contents
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    reports
}

fn is_safe(report: &Vec<i32>) -> bool {
    let diffs = Vec::as_slice(report)
        .windows(2)
        .map(|pair| pair[1] - pair[0])
        .collect::<Vec<_>>();

    let sign = diffs[0].signum();
    diffs
        .iter()
        .all(|&x| x.signum() == sign && 1 <= x.abs() && x.abs() <= 3)
}

fn subreports(report: &[i32]) -> Vec<Vec<i32>> {
    let mut subreps: Vec<Vec<i32>> = (0..report.len())
        .map(|i| {
            let mut subrep = report.to_owned();
            subrep.remove(i);
            subrep
        })
        .collect();

    subreps.push(report.to_owned());

    subreps
}

fn part1(reports: &[Vec<i32>]) {
    let result = reports.iter().map(is_safe).filter(|&x| x).count();

    println!("Result (Part 1): {}", result);
}

fn part2(reports: &[Vec<i32>]) {
    let result = reports
        .iter()
        .map(|report| subreports(report).iter().any(is_safe))
        .filter(|&x| x)
        .count();

    println!("Result (Part 2): {}", result);
}

fn main() {
    println!("*** DAY 2 ***");

    let file_path = "input.txt";
    let reports = parse_file(file_path);

    part1(&reports);
    part2(&reports);
}
