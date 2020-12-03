use std::fs;
fn main() {
    let map = fs::read_to_string(&"inputs/input03.txt".to_string()).expect("Could not open input");
    let counts = [(1,1),(3,1),(5,1),(7,1),(1,2)].iter().map(|dir| map.lines().step_by(dir.1).zip((0..).step_by(dir.0)).
    filter(|&(line,x)| line.as_bytes()[x % line.len()]=='#' as u8).count());
    println!("Product: {:?}", counts.product::<usize>());
}
