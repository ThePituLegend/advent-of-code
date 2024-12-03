use regex::Regex;
use std::fs;

#[derive(Clone, Copy, Debug)]
struct Mul {
    pos: i32,
    mul: (i32, i32),
}

impl Mul {
    fn calc(&self) -> i32 {
        self.mul.0 * self.mul.1
    }
}

#[derive(Debug)]
struct Modifier {
    pos: i32,
    enable: bool,
}

fn parse_file(file_path: &str) -> String {
    fs::read_to_string(file_path).expect("Failed to read the file")
}

fn find_muls(input: &str) -> Vec<Mul> {
    let re = Regex::new(r"mul\((?<st>[0-9]+),(?<nd>[0-9]+)\)")
        .expect("Something's wrong with RegEx (muls).");
    re.captures_iter(input)
        .map(|c| Mul {
            pos: c.get(0).unwrap().start() as i32,
            mul: (
                c["st"].parse::<i32>().unwrap(),
                c["nd"].parse::<i32>().unwrap(),
            ),
        })
        .collect()
}

fn find_modifiers(input: &str) -> Vec<Modifier> {
    let re_do = Regex::new(r"do\(\)").expect("Something's wrong with RegEx (do).");
    let re_dont = Regex::new(r"don't\(\)").expect("Something's wrong with RegEx (don't).");

    let mut modifiers: Vec<Modifier> = re_do
        .captures_iter(input)
        .map(|c| Modifier {
            pos: c.get(0).unwrap().start() as i32,
            enable: true,
        })
        .collect();

    modifiers.extend(re_dont.captures_iter(input).map(|c| Modifier {
        pos: c.get(0).unwrap().start() as i32,
        enable: false,
    }));

    modifiers.sort_by_key(|m| m.pos);
    modifiers
}

fn part1(muls: &[Mul]) {
    let result = muls.iter().fold(0, |acc, mul| acc + mul.calc());
    println!("Result (Part 1): {}", result);
}

fn part2(muls: &[Mul], mods: &[Modifier]) {
    let mut mods_iter = mods.iter().peekable();
    let mut enable = true;

    let result: i32 = muls
        .iter()
        .filter(|mul| {
            if let Some(m) = mods_iter.next_if(|m| mul.pos > m.pos) {
                enable = m.enable;
            }
            enable
        })
        .map(|mul| mul.calc())
        .sum();

    println!("Result (Part 2): {}", result);
}

fn main() {
    println!("*** DAY 3 ***");

    let file_path = "example.txt";
    let input = parse_file(file_path);

    let muls = find_muls(&input);
    let mods = find_modifiers(&input);

    part1(&muls);
    part2(&muls, &mods);
}
