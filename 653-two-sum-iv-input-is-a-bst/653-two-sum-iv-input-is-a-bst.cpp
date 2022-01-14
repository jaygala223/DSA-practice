/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class BstIterator{
    public:
    stack<TreeNode*> st;
    bool reverse = true;
    
    BstIterator(TreeNode* root, bool isReverse){
        reverse = isReverse;
        pushNextPrev(root);
    }
    
    void pushNextPrev(TreeNode* node){
        while(node){
            st.push(node);
            if(reverse) node = node->right;
            else node = node->left;
        }
    }
    
    int nextPrev(){
        TreeNode* node = st.top();
        st.pop();
        
        if(reverse) pushNextPrev(node->left);
        else pushNextPrev(node->right);
        return node->val;
    }
        
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        BstIterator n(root, false);
        BstIterator p(root, true);
        
        int i = n.nextPrev();
        int j = p.nextPrev();
        
        while(i<j){
            if(i+j == k) return true;
            
            else if(i+j > k){
                j = p.nextPrev();
            }
            else i = n.nextPrev();
        }
        return false;
    }
    
};