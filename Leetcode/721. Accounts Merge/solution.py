from typing import List, Dict

class DSU:
    def __init__(self, sz: int):
        self.representative = list(range(sz))  # Initially, each group is its own representative
        self.size = [1] * sz  # Initialize the size of all groups to 1

    def findRepresentative(self, x: int) -> int:
        if x == self.representative[x]:
            return x
        # Path compression
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]

    def unionBySize(self, a: int, b: int):
        repA = self.findRepresentative(a)
        repB = self.findRepresentative(b)

        # If nodes a and b already belong to the same group, do nothing.
        if repA == repB:
            return

        # Union by size: point the representative of the smaller group to the larger group.
        if self.size[repA] >= self.size[repB]:
            self.size[repA] += self.size[repB]
            self.representative[repB] = repA
        else:
            self.size[repB] += self.size[repA]
            self.representative[repA] = repB


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountListSize = len(accounts)
        dsu = DSU(accountListSize)
        emailGroup: Dict[str, int] = {}  # Maps email to their component index

        for i in range(accountListSize):
            accountSize = len(accounts[i])
            for j in range(1, accountSize):
                email = accounts[i][j]
                # If this is the first time seeing this email, assign component group as the account index
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    # If we have seen this email before, union this group with the previous group of the email
                    dsu.unionBySize(i, emailGroup[email])

        # Store emails corresponding to the component's representative
        components: Dict[int, List[str]] = {}
        for email, group in emailGroup.items():
            groupRep = dsu.findRepresentative(group)
            if groupRep not in components:
                components[groupRep] = []
            components[groupRep].append(email)

        # Sort the components and add the account name
        mergedAccounts = []
        for group, component in components.items():
            component.sort()  # Sort the emails
            component.insert(0, accounts[group][0])  # Add the account name at the beginning
            mergedAccounts.append(component)

        return mergedAccounts