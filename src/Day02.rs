use std::fs;
extern crate regex;
use regex::Regex;
fn main() {
    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let text = fs::read_to_string(&"inputs/input02.txt".to_string()).expect("Something is wrong I can feel it.");
    let mut part1: i32 = 0;
    let mut part2: i32 = 0;
    for cap in re.captures_iter(&text) {
        let val1: usize = cap[1].parse::<usize>().unwrap();
        let val2: usize = cap[2].parse::<usize>().unwrap();
        let rule: u8 = cap[3].to_string().as_bytes()[0];
        let pass = cap[4].to_string();
        let count = pass.rmatches(rule as char).count();
        if count>=val1 && count<=val2{
            part1+=1;
        }
        if (pass.as_bytes()[val1-1]==rule)!=(pass.as_bytes()[val2-1]==rule){
            part2+=1;
        }
    }
    println!("{:?}", part1);
    println!("{:?}", part2);
}
