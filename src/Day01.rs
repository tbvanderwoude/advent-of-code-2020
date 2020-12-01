use std::fs;
pub fn load_numbers(filename: &String) -> Vec<i32> {
    fs::read_to_string(filename).expect("Something is wrong I can feel it.").
    split("\n").
    filter(|x|{x.to_string().parse::<i32>().is_ok()}).
    map(|x| x.to_string().parse::<i32>().unwrap()).collect()
}
fn main() {
    let numbers = load_numbers(&"inputs/input01.txt".to_string());
    let mut part1: i32 = 0;
    let mut part2: i32 = 0;
    for x in &numbers
    {
        for y in &numbers{
            if x+y==2020{
                part1 = x*y;
            }
            for z in &numbers{
                if x+y+z==2020{
                    part2=x*y*z;
                }
            }
        }
    }
    println!("{:?}", part1);
    println!("{:?}", part2);
}
