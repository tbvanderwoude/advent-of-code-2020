use std::fs;
fn main() {
    let text = fs::read_to_string(&"inputs/input03.txt".to_string()).expect("Could not open input");
    let map = text.split("\n").collect::<Vec<&str>>();
    let directions: Vec<(usize,usize)> = vec![(1,1),(3,1),(5,1),(7,1),(1,2)];
    let counts = directions.iter().map(|dir| (0..(map.len().clone()-1)).filter(|y| y % dir.1==0).
    map(|y|( map[y].as_bytes()[(dir.0*y/dir.1) % map[0].len()]=='#' as u8) as i64).fold(0,|acc,x| acc+x));
    println!("Product: {:?}", counts.fold(1 ,|acc,x| acc*x));
}
