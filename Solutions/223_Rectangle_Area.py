class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        A1 = abs(C-A)*abs(D-B)
        A2 = abs(G-E)*abs(H-F)
        A3Length = max(min(max(A,C),max(E,G)) - max(min(A,C),min(E,G)), 0) 
        A3Width = max(min(max(B,D),max(H,F)) - max(min(B,D),min(H,F)) , 0)
        return A1 + A2 - A3Width * A3Length