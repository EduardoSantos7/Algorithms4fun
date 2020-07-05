fn main() {
    println!("val: {}", get_nth_fib(5));
}

fn get_nth_fib(n: i32) -> i32 {
    let mut mem = vec![0, 1];

    if n < 3 {
        return mem[(n - 1) as usize];
    }

    for _ in 3..n + 1 {
        let new_val = mem[0] + mem[1];
        mem[0] = mem[1];
        mem[1] = new_val;
    }
    mem[1]
}