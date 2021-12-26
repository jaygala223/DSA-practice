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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || head->next == NULL) return head;
        
        ListNode* dummy = head;
        int cnt = 1;
        
        while(dummy->next){
            cnt++;
            dummy=dummy->next;
        }
        dummy->next = head;
        
        int rotation;
        rotation = cnt - (k%cnt);
        
        ListNode* newh;
        
        for(int i=0; i<rotation; i++) dummy=dummy->next;
        
        newh = dummy->next;
        dummy->next = NULL;
        
        return newh;
    }
};