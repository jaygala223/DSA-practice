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
public:
    int kthSmallest(TreeNode* root, int k) {
        if(!root) return -1;
        
        int i=0, ans=0;
        
        TreeNode* curr = root;
        while(curr!=NULL){
            if(curr->left == NULL){
                i++;
                if(i==k) ans = curr->val; 
                curr = curr->right;
            }
            else{
                TreeNode* thread = curr->left;
                while(thread->right && thread->right != curr){
                    thread = thread->right;
                }
                
                //thread create
                if(thread->right == NULL){
                    thread->right = curr;
                    curr = curr->left;
                }
                
                //thread break
                else{
                    thread->right = NULL;
                    i++;
                    if(i==k) ans = curr->val;
                    curr = curr->right;
                }
            }
        }
        return ans;
    }
};