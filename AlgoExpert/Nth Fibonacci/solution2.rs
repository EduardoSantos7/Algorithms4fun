use std::collections::HashMap;

fn main() {
    let mut mem = HashMap::new();
    mem.insert(1, 0);
    mem.insert(2, 1);
    let val = get_nth_fib(7, &mut mem);
    println!("val: {}", val);
}

fn get_nth_fib(n: i32, mem: &mut HashMap<i32, i32>) -> i32 {
    if mem.get(&n).is_some() {
        return *mem.get(&n).unwrap()
    }
    let a = get_nth_fib(n - 1, mem);
    let b = get_nth_fib(n - 2, mem);
    mem.insert(n, a + b);
    return *mem.get(&n).unwrap()
}