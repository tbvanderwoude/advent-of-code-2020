use std::fs;
extern crate regex;
use regex::Regex;
fn main() {
    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let text = fs::read_to_string(&"inputs/input03.txt".to_string()).expect("Something is wrong I can feel it.");
    let map = text.split("\n").collect::<Vec<&str>>();
    let directions = [(1,1),(3,1),(5,1),(7,1),(1,2)];
    let mut counts = vec![];
    let mut prod: i64 = 1;
    for dir in directions.iter(){
        let mut x = 0;
        let mut y = 0;
        let mut tree_count = 0;
        let final_x: usize = map[0].len();
        let final_y: usize = map.len().clone()-1;
        while y<final_y{
            if map[y].as_bytes()[x%final_x]=='#' as u8
            {
                tree_count+=1;
            }
            x+=dir.0;
            y+=dir.1;
        }
        prod = prod*tree_count;
        counts.push(tree_count);
        print!("{:?}: {} trees", dir,tree_count);
    }
    print!("{:?}", prod);
}
