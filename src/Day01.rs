use std::fs;
#[macro_export]
macro_rules! aoc {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
}

fn main() {
    let text = fs::read_to_string(&"inputs/input01.txt".to_string()).expect("error reading file");
    let numbers = text.lines().filter(|x|{x.to_string().parse::<i32>().is_ok()}).map(|x| x.to_string().parse::<i32>().unwrap()).collect::<Vec<i32>>();
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
