use std::collections::{HashMap, HashSet};
use std::fs;
use std::ops::Index;

fn parse_file(file_path: &str) -> (Vec<String>, Vec<String>) {
    let input = fs::read_to_string(file_path)
        .expect("Failed to read the file")
        .lines()
        .map(String::from)
        .collect::<Vec<String>>();
    let input = input.split(String::is_empty).collect::<Vec<&[String]>>();

    (input[0].to_vec(), input[1].to_vec())
}

fn process_order(order: &[String]) -> HashMap<u32, HashSet<u32>> {
    let mut dict: HashMap<u32, HashSet<u32>> = HashMap::new();

    for s in order {
        let (x, y) = s.split_once('|').unwrap();
        dict.entry(x.parse().unwrap())
            .or_default()
            .insert(y.parse().unwrap());
    }

    dict
}

fn process_updates(updates: &[String]) -> Vec<Vec<u32>> {
    updates
        .iter()
        .map(|u| u.split(",").map(|x| x.parse().unwrap()).collect())
        .collect()
}

fn check_order(order: &HashMap<u32, HashSet<u32>>, update: &[u32]) -> bool {
    order.iter().all(|(k, v)| {
        v.iter().all(|&dep| {
            update
                .iter()
                .position(|x| x == k)
                .zip(update.iter().position(|x| x == &dep))
                .map_or(true, |(l, r)| l < r)
        })
    })
}

fn reorder_update(order: &HashMap<u32, HashSet<u32>>, mut update: Vec<u32>) -> Vec<u32> {
    update.sort_by(|a, b| {
        if check_order(order, &[*a, *b]) {
            std::cmp::Ordering::Less
        } else {
            std::cmp::Ordering::Greater
        }
    });

    update
}

fn find_middle(update: &[u32]) -> u32 {
    *update.index(update.len()/2)
}

fn part1(order: &HashMap<u32, HashSet<u32>>, updates: &[Vec<u32>]) {
    let result = updates
        .iter()
        .filter(|u| check_order(order, u))
        .fold(0, |acc, u| {
            acc + find_middle(u)
        });

    println!("Result (Part 1): {}", result);
}

fn part2(order: &HashMap<u32, HashSet<u32>>, updates: &[Vec<u32>]) {
    let result = updates
        .iter()
        .filter(|u| !check_order(order, u)) // only check incorrectly ordered updates
        .fold(0, |acc, u| {
            let reordered = reorder_update(order, u.clone());
            acc + find_middle(&reordered)
        });

    println!("Result (Part 2): {}", result);
}

fn main() {
    println!("*** DAY 5 ***");

    let file_path = "input.txt";
    let (order, updates) = parse_file(file_path);
    let order = process_order(&order);
    let updates = process_updates(&updates);

    part1(&order, &updates);
    part2(&order, &updates);
}
