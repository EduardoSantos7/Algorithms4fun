fn main() {
    println!("val: {}", get_nth_fib(1));
}

fn get_nth_fib(n: i32) -> i32 {
    if n == 1 {
        return 0;
    }
    else if n == 2{
        return 1;
    }
    return get_nth_fib(n - 1) + get_nth_fib(n - 2)
}