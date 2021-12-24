/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* prev = new ListNode(0);
    
        prev->next = head;
        ListNode* curr = prev;
        
        
        while(curr->next && curr->next->next){
            if(curr->next->val == curr->next->next->val){
                int dup = curr->next->val;
                while(curr->next && dup == curr->next->val){
                    curr->next = curr->next->next;
                }    
            }
            else curr = curr->next;
        }
        return prev->next;
    }
};