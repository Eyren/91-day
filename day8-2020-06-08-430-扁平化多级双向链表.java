class Solution {
    private Node prev = null;
    public Node flatten(Node head) {
        dfs(head);
        return head;
    }
    
    private void dfs(Node head) {
        if (head == null) return;
        Node next = head.next;
        if (prev != null) {
            prev.next = head;
            head.prev = prev;
        }
        prev = head;
        dfs(head.child);
        head.child = null;
        dfs(next);
    }
}
