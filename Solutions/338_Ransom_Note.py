class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomDict = collections.Counter(ransomNote)
        magazineDict = collections.Counter(magazine)

        for char in ransomDict:
        	if char not in magazineDict or magazineDict[char] < ransomDict[char]:
        		return False
        return True


-----------------------------------------------------------
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not (collections.Counter(magazine) - collections.Counter(ransomNote))