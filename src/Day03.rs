use std::fs;
fn main() {
    let map = fs::read_to_string(&"inputs/input03.txt".to_string()).expect("Could not open input");
    let dirs = [(1,1),(3,1),(5,1),(7,1),(1,2)];
    let counts = dirs.iter().map(|dir| map.lines().step_by(dir.1).zip((0..).step_by(dir.0)).
    filter(|&(line,x)| line.as_bytes()[x % line.len()]=='#' as u8).count()).collect::<Vec<usize>>();
    println!("Trees encountered for each of the slopes: {:?}",dirs.iter().cloned().zip(counts.iter().cloned()).collect::<Vec<((usize,usize),usize)>>());
    println!("Product of these counts: {:?}", counts.iter().product::<usize>());
}
