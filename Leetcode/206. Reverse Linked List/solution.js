// Made in 11/01/2018 08:48

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var currentNext;
    var last = null;
    var temp = head;

    while (temp != null) {
        currentNext = temp.next;
        temp.next = last;
        last = temp;
        temp = currentNext;
    }
    return last;
};