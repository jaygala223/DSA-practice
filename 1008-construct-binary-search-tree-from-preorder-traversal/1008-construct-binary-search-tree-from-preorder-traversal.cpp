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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i=0;
        
        return buildTree(preorder, i, INT_MAX);
    }
    
    TreeNode* buildTree(vector<int>& preorder, int& i, int upperBound){
        if(i == preorder.size() || preorder[i] > upperBound) return NULL;
        
        TreeNode* root = new TreeNode(preorder[i++]);
        
        root->left = buildTree(preorder, i, root->val);
        root->right = buildTree(preorder, i, upperBound);
        
        return root;
    }
};