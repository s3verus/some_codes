use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("fail to read input!");
    let mut input_vec = input.trim().split(", ")
        .collect::<Vec<&str>>();
    
//    let maxim = input_vec.iter().max();
//    let maxim = match maxim {
//        Some(max) => max,
//        None      => "Vector is empty",
//    };

    let mut maxim = my_longest::maxim(&input_vec); 
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
                maxim = my_longest::maxim(&input_vec);
                break;
            }
            iner_count += 1;
        }
        vec_index += 1;

    }
    println!("{}", maxim);
}
