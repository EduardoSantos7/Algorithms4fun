/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* start;

bool recursiveHelper(struct ListNode* head) {
    if(head) {
        if(!recursiveHelper(head->next))
            return false;
        if(start->val != head->val)
            return false;
        start = start->next;
    }

    return true;
}

bool isPalindrome(struct ListNode* head){
    start = head;
    return recursiveHelper(head);
}