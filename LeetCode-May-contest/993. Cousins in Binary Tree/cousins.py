class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(root,parent,level,value):
            if root:
                if root.val==value:
                    return level,parent
                return dfs(root.left,root,level+1,value) or dfs(root.right,root,level+1,value)
        lx,px=dfs(root,None,0,x)
        ly,py=dfs(root,None,0,y)
            
        return lx==ly and px!=py
