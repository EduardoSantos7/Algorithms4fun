// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut num = 0;
        let mut temp = head;
        
        while temp != None {
            num <<= 1;
            if let Some(x) = &temp {
                if x.val == 1 {
                    num += 1;   
                }
            }
            if let Some(h) = temp{
              temp = h.next;   
            }
        }
        
        num
    }
}