pub fn maxim<'a>(input_vec: &'a Vec<&str>) -> &'a str {
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
