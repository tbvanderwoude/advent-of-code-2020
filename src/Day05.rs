use std::fs;
use std::collections::{HashSet, HashMap};

fn main() {
    let text = fs::read_to_string(&"inputs/input05.txt".to_string()).expect("Error");
    let map: HashMap<char,i32> = [('F',0),('B',1),('L',0),('R',1)].iter().cloned().collect();
    let mut sids = text.lines().map(|s| s.bytes().map(|b| map.get(&(b as char)).unwrap()).fold(0, |acc, x|acc*2+x)).collect::<Vec<i32>>();
    sids.sort();
    let maxseat = sids.iter().max().unwrap();
    let seat = sids.iter().zip(sids.split_at(1).1.iter()).filter(|(x,y)| **y-**x==2).next().unwrap().0+1;
    println!("{}",maxseat);
    println!("{}",seat)
}
