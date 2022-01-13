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
    vector<int>in;
    void inorder(TreeNode* root){
        if(!root) return;
        inorder(root->left);
        in.push_back(root->val);
        inorder(root->right);
    }
    
    bool findTarget(TreeNode* root, int k) {
        inorder(root);
        
        int left=0, right= (in.size()-1);
        
        while(left < right){
            if(in[left] + in[right] == k) return true; 
            else if(in[left] + in[right] > k) right--;
            else left++;
        }
        return false;
    }
};