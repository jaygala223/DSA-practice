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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int k = lists.size();
        
        if(k==0) return NULL;
        
        priority_queue<int, vector<int>, greater<int>> hp;
        
        for(auto item: lists){
            if(item == NULL) continue;
            ListNode* curr = item;
            while(curr){
                hp.push(curr->val);
                curr=curr->next;
            }
        }
        
        if(hp.empty()) return NULL;
        ListNode* h1 = new ListNode(hp.top());
        ListNode* temp = h1;
        hp.pop();
        
        while(!hp.empty()){
            ListNode* temp2 = new ListNode(hp.top());
            hp.pop();
            
            temp->next = temp2;
            temp = temp2;
        }
        temp->next = NULL;
        return h1;
    }
};




