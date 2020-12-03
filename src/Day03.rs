use std::fs;
fn main() {
    let text = fs::read_to_string(&"inputs/input03.txt".to_string()).expect("Could not open input");
    let map = text.split("\n").collect::<Vec<&str>>();
    let directions = [(1,1),(3,1),(5,1),(7,1),(1,2)];
    let mut counts = vec![];
    for dir in directions.iter(){
        let final_x: usize = map[0].len();
        let final_y: usize = map.len().clone()-1;
        let tree_count: i64 = (0..final_y).filter(|y| y % dir.1==0).map(|y|( map[y].as_bytes()[(dir.0*y/dir.1) % final_x]=='#' as u8) as i64).fold(0,|acc,x| acc+x);
        counts.push(tree_count);
        println!("{:?}: {} trees", dir,tree_count);
    }
    println!("Product: {:?}", counts.iter().fold(1 ,|acc,x| acc*x));
}
