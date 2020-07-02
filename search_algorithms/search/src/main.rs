use std::time::Instant;

/**
 * Complexity: Time: O(N), Space: O(1)
 */
fn linear_search<T: PartialEq + Copy>(list: &[T], target: T) -> Option<usize> {
    for elem in 0..list.len() {
        if list[elem] == target {
            return Some(elem);
        }
    }
    None
}

/**
 * Complexity: Time: O(log N), Space: O(1)
 */
fn binary_search<T: PartialEq + PartialOrd + Copy>(list: &[T], target: T) -> Option<usize> {
    let mut left = 0;
    let mut right = list.len() - 1;

    while left <= right {
        let mid = (right - left) / 2 + left;
        if list[mid] > target {
            right = mid - 1;
        }
        else if list[mid] < target {
            left = mid + 1;
        }
        else {
            return Some(mid);
        }
    }
    None
}

/**
 * Complexity: Time: O(√N), Space: O(1)
 * M = floor(√N)
 * Worst Time Complexity: O(N/M + M - 1) ≈ O(N)
 */
fn jump_search<T: PartialEq + PartialOrd + Copy>(list: &[T], target: T) -> Option<usize> {
    let jump: usize = (list.len() as f32).sqrt() as usize;
    let len = list.len();
    let last_index = len - 1;
    let mut i = 0;
    let mut prev = 0;

    if len == 0 {
        return None;
    }

    while list[i] < target {
        prev = i;
        i += jump;
        if i > last_index {
            i = last_index;
        }
        if prev >= len {
            return None;
        }
    }

    for index in prev..(i + 1) {
        if list[index] == target {
            return Some(index);
        }
    }

    None
}

/**
 * Complexity: Time: O(log N), Space: O(1)
 * This is an improvement over Binary Search.
 * The idea is to start near to the target instead the middle.
 */

fn interpolation_search(list: &[i32], target: i32) -> Option<usize>{
    let mut left: usize = 0;
    let mut right = list.len() as usize - 1;
    let t = target - list[left];

    while left <= right {
        let pos = left + (((t as usize) * (right - left) / (list[right] - list[left]) as usize ));
        if list[pos] > target {
            right = pos - 1;
        }
        else if list[pos] < target {
            left = pos + 1;
        }
        else {
            return Some(pos);
        }
    }
    None

}

/**
 * Complexity: Time: O(log N), Space: O(1)
 */
fn exponential_search<T: PartialEq + PartialOrd + Copy>(list: &[T], target: T) -> Option<usize> {
    if list[0] == target{
        return Some(0);
    }
    // Find a sub array where the targett could be
    let mut i = 1;
    while i < list.len() && list[i] < target {
        i *= 2;
    }

    // Do Binary Search in the sub array
    let mut left = i/2;
    let mut right = i;

    while left <= right {
        let mid = (right - left) / 2 + left;
        if list[mid] > target {
            right = mid - 1;
        }
        else if list[mid] < target {
            left = mid + 1;
        }
        else {
            return Some(mid);
        }
    }

    None
}




fn main() {
    let nums = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
    let target = 2;

    let mut start = Instant::now();
    let res = linear_search(&nums, target).expect("No lo encontre");
    let duration = start.elapsed();

    start = Instant::now();
    let res2 = binary_search(&nums, target).expect("No lo encontre");
    let duration_2 = start.elapsed();

    start = Instant::now();
    let res3 = jump_search(&nums, target).expect("No lo encontre");
    let duration_3 = start.elapsed();

    start = Instant::now();
    let res4 = interpolation_search(&nums, target).expect("No lo encontre");
    let duration_4 = start.elapsed();

    start = Instant::now();
    let res5 = exponential_search(&nums, target).expect("No lo encontre");
    let duration_5 = start.elapsed();

    print!("El número se encontró LS: {} in {:?}\n", res, duration);
    print!("El número se encontró BS: {} in {:?}\n", res2, duration_2);
    print!("El número se encontró JS: {} in {:?}\n", res3, duration_3);
    print!("El número se encontró IS: {} in {:?}\n", res4, duration_4);
    print!("El número se encontró ES: {} in {:?}\n", res5, duration_5);
}
