use itertools::Itertools;
use std::collections::{HashMap, HashSet};
use std::fs;

#[derive(Debug, Eq, Hash, PartialEq, Clone, Copy)]
struct Pos {
    r: i32,
    c: i32,
}

fn parse_file(file_path: &str) -> (HashMap<char, HashSet<Pos>>, Pos) {
    let input = fs::read_to_string(file_path).expect("Failed to read the file");

    let size = Pos {
        // Abusing Pos struct to hold a size
        r: input.lines().count() as i32,
        c: input.lines().next().map_or(0, |line| line.len()) as i32,
    };

    let antennas = input
        .lines()
        .enumerate()
        .flat_map(|(row, line)| {
            line.chars()
                .enumerate()
                .filter(|&(_, c)| c != '.')
                .map(move |(col, freq)| {
                    (freq, Pos {
                        r: row as i32,
                        c: col as i32,
                    })
                })
        })
        .fold(
            HashMap::new(),
            |mut map: HashMap<char, HashSet<Pos>>, (c, pos)| {
                map.entry(c).or_default().insert(pos);
                map
            },
        );

    (antennas, size)
}

fn check_inbounds(p: &Pos, size: &Pos) -> bool {
    (0 <= p.r) && (p.r < size.r) && (0 <= p.c) && (p.c < size.c)
}

fn opposite_ends(p1: &Pos, p2: &Pos, size: &Pos) -> Vec<Pos> {
    let (dr, dc) = (p2.r - p1.r, p2.c - p1.c);
    let positions = vec![
        Pos { r: p1.r - dr, c: p1.c - dc },
        Pos { r: p2.r + dr, c: p2.c + dc },
    ];

    positions.into_iter().filter(|p| check_inbounds(p, size)).collect() // Only inbound antinodes
}

fn dotted_line(p1: &Pos, p2: &Pos, size: &Pos) -> Vec<Pos> {
    let (dr, dc) = (p2.r - p1.r, p2.c - p1.c);
    let mut antinodes = Vec::new();

    let mut pos = Pos { r: p2.r, c: p2.c };
    while check_inbounds(&pos, size) {
        antinodes.push(pos);
        pos.r -= dr;
        pos.c -= dc;
    }

    pos = Pos { r: p1.r, c: p1.c };
    while check_inbounds(&pos, size) {
        antinodes.push(pos);
        pos.r += dr;
        pos.c += dc;
    }

    antinodes
}

fn part(
    n: u32,
    antennas: &HashMap<char, HashSet<Pos>>,
    size: &Pos,
    generate: fn(&Pos, &Pos, &Pos) -> Vec<Pos>,
) {
    let antinodes: HashSet<Pos> = antennas
        .iter()
        .flat_map(|(_, positions)| positions.iter().combinations(2))
        .flat_map(|pair| generate(pair[0], pair[1], size))
        .collect();

    println!("Result (Part {n}): {}", antinodes.len());
}

fn main() {
    println!("*** DAY 8 ***");

    let file_path = "input.txt";
    let (antennas, size) = parse_file(file_path);

    part(1, &antennas, &size, opposite_ends);
    part(2, &antennas, &size, dotted_line);
}
