use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("fail to read input!");
    let input_vec = input.trim().split(", ")
        .collect::<Vec<&str>>();

    my_longest::longest_valid_item(input_vec);
}
