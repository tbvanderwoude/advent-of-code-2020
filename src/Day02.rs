use std::fs;
extern crate regex;
use regex::Regex;
fn main() {
    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let text = fs::read_to_string(&"inputs/input02.txt".to_string()).expect("Something is wrong I can feel it.");
    let mut part1: i32 = 0;
    let mut part2: i32 = 0;
    let proc_caps = re.captures_iter(&text)
                      .map(|cap|(cap[1].parse::<usize>().unwrap(),cap[2].parse::<usize>().unwrap(),cap[3].to_string().as_bytes()[0],cap[4].to_string()));
    for (rule_val1,rule_val2,symbol,pass) in proc_caps {
        let count = pass.rmatches(symbol as char).count();
        if count>=rule_val1 && count<=rule_val2{
            part1+=1;
        }
        if (pass.as_bytes()[rule_val1-1]==symbol)!=(pass.as_bytes()[rule_val2-1]==symbol){
            part2+=1;
        }
    }
    println!("Passwords correct under first policy: {:?}", part1);
    println!("Passwords correct under second policy: {:?}", part2);
}
