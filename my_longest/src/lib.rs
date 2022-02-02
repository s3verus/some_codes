mod work_with_vec {
    pub mod iter_items {
//    let maxim = input_vec.iter().max();
//    let maxim = match maxim {
//        Some(max) => max,
//        None      => "Vector is empty",
//    };
        pub fn maxim<'a>(input_vec: &'a Vec<&str>) -> &'a str {
            // get vector of &str and return &str with maximum len
            let mut maxim = "";
            let mut maxim_len = 0;
            for item in input_vec {
                if maxim_len <= item.chars().count() {
                    maxim_len = item.chars().count();
                    maxim = item;
                }
            }
            maxim
        }
    }
}

use crate::work_with_vec::iter_items;

pub fn longest_valid_item(mut input_vec: Vec<&str>) -> String {
    let mut maxim = iter_items::maxim(&input_vec); 
    let bad_guys = String::from("cgijklmnopqsuvwxz");
    let mut vec_index = 0;
    let mut iner_count = 0;
    let len = input_vec.len();

    while vec_index < len {
        while iner_count < maxim.chars().count() {
            if bad_guys.contains(&maxim[iner_count..iner_count+1]) {
                // find index of maxim and remove
                let index = input_vec.iter().position(|x| *x == maxim).unwrap();
                input_vec.remove(index);
                maxim = iter_items::maxim(&input_vec);
                break;
            }
            iner_count += 1;
        }
        vec_index += 1;
    }
    println!("{}", maxim);
    maxim.to_string() 
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn same_len() {
        let input_vec = vec!["bat", "tab", "tad"];
        assert_eq!("tad", longest_valid_item(input_vec));
    }

    #[test]
    fn have_one() {
        let input_vec = vec!["bat"];
        assert_eq!("bat", longest_valid_item(input_vec));
    }
}
