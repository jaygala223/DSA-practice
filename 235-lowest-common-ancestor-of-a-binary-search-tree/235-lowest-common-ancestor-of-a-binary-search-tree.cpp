/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) return NULL;
        
        int pv = p->val, qv = q->val;
        
        while(root != NULL){
            int rv = root->val;
            
            if((pv > rv and qv < rv) || (pv < rv and qv > rv)){
                return root;
            }
            
            if(root == p || root == q){
                return root==p?p:q;
            }
            if(pv > rv) root = root->right;
            else root = root->left;
        }
        return NULL;
    }
};