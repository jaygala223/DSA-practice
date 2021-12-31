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
    //morris traversal
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder;
        if(!root) return inorder;
        
        TreeNode* curr = root;
        while(curr!=NULL){
            if(curr->left == NULL){
                inorder.push_back(curr->val);
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
                    inorder.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }
        return inorder;
    }
};




