struct NumArray {
    acum: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        let mut acum = Vec::new();
        acum.push(nums[0]);
        for i in 1..nums.len() {
            acum.push(nums[i] + acum[i-1]);
        }
        NumArray{acum}
    }
    
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        if left != 0 {
            return self.acum[right as usize] - self.acum[left as usize -1];
        }
        return self.acum[right as usize];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */
