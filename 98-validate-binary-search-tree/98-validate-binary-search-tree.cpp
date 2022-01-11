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
    bool validater(TreeNode* node, long left, long right){
        
        if(node == NULL) return true;
        
        bool left_tree = validater(node->left, left, node->val);
        bool right_tree = validater(node->right, node->val, right);
        
        if(node->val >= right || node->val <= left) return false; 
        else return (left_tree && right_tree);
    }
    
    bool isValidBST(TreeNode* root) {
        long left = LONG_MIN, right = LONG_MAX;
        
        return validater(root, left, right);
    }
};