use std::collections::HashSet;
use std::fs;

#[derive(Eq, Hash, PartialEq, Clone, Copy)]
struct Pos {
    r: i32,
    c: i32,
}

const DIRECTIONS: [(i32, i32); 4] = [
    (-1, 0), // Up
    (0, 1),  // Right
    (1, 0),  // Down
    (0, -1), // Left
];

fn parse_file(file_path: &str) -> (Vec<Vec<bool>>, Pos) {
    // Read the input file into a string
    fs::read_to_string(file_path)
        .expect("Failed to read the file")
        .lines()
        .enumerate()
        .fold(
            (Vec::new(), Pos { r: 0, c: 0 }),
            |(mut matrix, mut position), (i, line)| {
                let row = line
                    .chars()
                    .enumerate()
                    .map(|(j, char)| match char {
                        '.' => true,
                        '#' => false,
                        _ => {
                            position = Pos {
                                r: i as i32,
                                c: j as i32,
                            }; // Note the position of the guard
                            true
                        }
                    })
                    .collect::<Vec<bool>>();

                matrix.push(row);
                (matrix, position)
            },
        )
}

fn move_guard(map: &[Vec<bool>], guard: Pos) -> HashSet<Pos> {
    let mut dir = 0;
    let mut visited: HashSet<Pos> = HashSet::new();
    let mut pos = Pos {
        r: guard.r + DIRECTIONS[dir].0,
        c: guard.c + DIRECTIONS[dir].1,
    };

    visited.insert(guard);

    while let Some(spot) = map.get(pos.r as usize).and_then(|r| r.get(pos.c as usize)) {
        if *spot {
            visited.insert(pos);
        } else {
            pos.r -= DIRECTIONS[dir].0;
            pos.c -= DIRECTIONS[dir].1;
            dir = (dir + 1) % 4;
        }

        pos.r += DIRECTIONS[dir].0;
        pos.c += DIRECTIONS[dir].1;
    }

    visited
}

fn loop_checker(map: &[Vec<bool>], guard: Pos) -> bool {
    let mut blockers: HashSet<(Pos, usize)> = HashSet::new(); // Store blockers and blocking direction
    let mut dir = 0;
    let mut pos = Pos {
        r: guard.r + DIRECTIONS[dir].0,
        c: guard.c + DIRECTIONS[dir].1,
    };

    while let Some(spot) = map.get(pos.r as usize).and_then(|r| r.get(pos.c as usize)) {
        if !*spot {
            if blockers.contains(&(pos, dir)) {
                return true;
            }

            blockers.insert((pos, dir));

            pos.r -= DIRECTIONS[dir].0;
            pos.c -= DIRECTIONS[dir].1;
            dir = (dir + 1) % 4;
        }

        pos.r += DIRECTIONS[dir].0;
        pos.c += DIRECTIONS[dir].1;
    }

    false
}

fn part1(map: &[Vec<bool>], guard: Pos) {
    let result = move_guard(map, guard);
    println!("Result (Part 1): {}", result.len());
}

fn part2(map: &[Vec<bool>], guard: Pos) {
    let path = move_guard(map, guard);

    let result = path.iter().fold(0, |acc, pos| {
        let mut map2 = map.to_owned();
        map2[pos.r as usize][pos.c as usize] = false; // Add blocker in path
        acc + loop_checker(&map2, guard) as u32
    });

    println!("Result (Part 2): {}", result);
}

fn main() {
    println!("*** DAY 6 ***");

    let file_path = "input.txt";
    let (map, guard) = parse_file(file_path);

    part1(&map, guard);
    part2(&map, guard);
}
