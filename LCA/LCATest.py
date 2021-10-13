import unittest
import LCA


class TestLCA(unittest.TestCase):
  
    def test_null_tree(self):
        #Null provided Binary Tree (Root is none).

        root = None
        result = LCA.findLCA(root, 1, 2)
        self.assertEqual(result, None)

    def test_BTree(self):
        # Test LCA statements with provided BT.

        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)

        result1 = LCA.findLCA(root, 4, 5).key
        result2 = LCA.findLCA(root, 5, 3).key

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    def test_lca_node(self):
        #Test when one of the provided nodes is the LCA.

        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)

        result = LCA.findLCA(root, 4, 2).key
        self.assertEqual(result, 2)

    def test_branched_tree(self):
        #Test one-side branched Binary Tree.

        root = LCA.Node(1)
        root.right = LCA.Node(2)
        root.right.right = LCA.Node(3)
        root.right.right.right = LCA.Node(4)

        result = LCA.findLCA(root, 4, 3).key
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()