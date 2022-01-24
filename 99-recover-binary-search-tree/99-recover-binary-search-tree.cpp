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
class Solution {
private:
    TreeNode* last;
    TreeNode* first; 
    TreeNode* middle;
    TreeNode* prev;
    int cnt = 0;
public:
    void inorder(TreeNode* root){
        if(!root) return;
        
        inorder(root->left);
        
        if(prev!=NULL && (prev->val > root->val)){
            //if first violation
            if(first == NULL){
                first = prev;
                middle = root;
            }
            //second violation
            else last = root;
        }
        //mark this as previous
        prev = root;
        inorder(root->right);
    }
    
    void recoverTree(TreeNode* root) {
        first = middle = last = NULL;
        prev = new TreeNode(INT_MIN);
        inorder(root);
        
        if(first && last) swap(first->val, last->val);
        
        //else if isiliye kyuki aisa bhi ho sakta hai 
        //ki koi violation ho hi nahi
        else  swap(first->val, middle->val);
            //if (first && middle) swap(first->val, middle->val);
        
    }
};