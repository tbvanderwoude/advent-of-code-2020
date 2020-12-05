use std::fs;
use std::collections::{HashSet, HashMap};
use regex::bytes::Regex;
#[macro_use] extern crate lazy_static;

fn check_field(name: &str, value: &str)-> bool{
    lazy_static! {
        static ref EXPRESSIONS: HashMap<String, Regex>  =
            [("byr".to_string(),Regex::new(r"^19[2-9]\d|200[0-2]$").unwrap()),
                ("iyr".to_string(),Regex::new(r"^201\d|2020$").unwrap()),
                ("eyr".to_string(),Regex::new(r"^202\d|2030$").unwrap()),
                ("hgt".to_string(),Regex::new(r"^(15\d|1[6-8]\d|19[0-3])cm|(59|6\d|7[0-6])in$").unwrap()),
                ("hcl".to_string(),Regex::new(r"^#[0-9|a-f]{6}$").unwrap()),
                ("ecl".to_string(),Regex::new(r"^amb|blu|brn|gry|grn|hzl|oth$").unwrap()),
                ("pid".to_string(),Regex::new(r"^\d{9}$").unwrap())
            ].iter().cloned().collect();
    }
    !EXPRESSIONS.contains_key(name)||EXPRESSIONS.get(name).unwrap().is_match(value.as_ref())
}
fn main() {
    let text = fs::read_to_string(&"inputs/input04.txt".to_string()).expect("Something is wrong I can feel it.");
    let passports= text.split("\n\n").map(|s| s.to_string());

    let mut present_count = 0;
    let mut correct_count = 0;
    let required_set = vec!["byr","iyr","eyr","hgt","hcl","ecl","pid"].into_iter().clone().collect::<HashSet<&str>>();
    for passport in passports{
        let mut fields = HashSet::new();
        let mut correct_fields = HashSet::new();
        for entry in passport.split_ascii_whitespace() {
            let parts = entry.split(":").collect::<Vec<&str>>();
            fields.insert(parts[0]);
            if check_field(parts[0],parts[1]){
                correct_fields.insert(parts[0]);
            }
        }
        present_count+=fields.is_superset(&required_set) as i32;
        correct_count+=correct_fields.is_superset(&required_set) as i32;
    }
    println!("Passports with all necessary fields present: {}",present_count);
    println!("Passports with all necessary fields valid: {}",correct_count);
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_byr() {
        assert!(!check_field("byr","1919"));
        assert!(check_field("byr","1920"));
        assert!(check_field("byr","2002"));
        assert!(!check_field("byr","2003"));
    }
    #[test]
    fn test_iyr() {
        assert!(!check_field("iyr","2009"));
        assert!(check_field("iyr","2010"));
        assert!(check_field("iyr","2020"));
        assert!(!check_field("iyr","2021"));
    }
    #[test]
    fn test_eyr() {
        assert!(!check_field("eyr","2019"));
        assert!(check_field("eyr","2020"));
        assert!(check_field("eyr","2030"));
        assert!(!check_field("eyr","2031"));
    }
    #[test]
    fn test_hgt() {
        assert!(!check_field("hgt","149cm"));
        assert!(check_field("hgt","150cm"));
        assert!(check_field("hgt","193cm"));
        assert!(!check_field("hgt","194cm"));
        assert!(!check_field("hgt","58in"));
        assert!(check_field("hgt","59in"));
        assert!(check_field("hgt","76in"));
        assert!(!check_field("hgt","77in"));
    }
    #[test]
    fn test_hcl() {
        assert!(!check_field("hcl","#1030a"));
        assert!(!check_field("hcl","#b29af2a"));
        assert!(check_field("hcl","#b29af2"));
        assert!(!check_field("hcl","#''''''"));
    }
    #[test]
    fn test_ecl() {
        assert!(!check_field("ecl","brun"));
        assert!(check_field("ecl","brn"));
    }
}
