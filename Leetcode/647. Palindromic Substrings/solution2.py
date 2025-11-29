class Solution:
    def countSubstrings(self, s: str) -> int:
        d1, d2 = self.manacher(s)
        # Cada centro i aporta d1[i] palíndromos impares y d2[i] pares
        return sum(d1) + sum(d2)
    
    def manacher(self, s: str) -> Tuple[List[int], List[int]]:
        """
        Devuelve dos listas:
        d1[i]: número de palíndromos de longitud impar centrados en i
            (longitudes 1, 3, 5, ..., hasta 2*d1[i]-1)
        d2[i]: número de palíndromos de longitud par centrados entre i-1 e i
            (longitudes 2, 4, 6, ..., hasta 2*d2[i])
        Complejidad: O(n)
        """
        n = len(s)

        # Palíndromos de longitud impar
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            # k es el "radio" inicial
            if i > r:
                k = 1
            else:
                k = min(d1[l + r - i], r - i + 1)
            # expandimos mientras siga siendo palíndromo
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            # actualizamos el palíndromo más a la derecha
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        # Palíndromos de longitud par
        d2 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            if i > r:
                k = 0
            else:
                k = min(d2[l + r - i + 1], r - i + 1)
            while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        return d1, d2
    
# Single loop


# from typing import List, Tuple

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         d1, d2 = self.manacher(s)
#         return sum(d1) + sum(d2)

#     def manacher(self, s: str) -> Tuple[List[int], List[int]]:
#         n = len(s)
#         if n == 0:
#             return [], []

#         d1 = [0] * n  # radios impares
#         d2 = [0] * n  # radios pares

#         # Estado para impares
#         l1, r1 = 0, -1
#         # Estado para pares
#         l2, r2 = 0, -1

#         for i in range(n):
#             # ---------- palíndromos impares ----------
#             if i > r1:
#                 k = 1
#             else:
#                 k = min(d1[l1 + r1 - i], r1 - i + 1)

#             while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
#                 k += 1

#             d1[i] = k
#             if i + k - 1 > r1:
#                 l1 = i - k + 1
#                 r1 = i + k - 1

#             # ---------- palíndromos pares ----------
#             if i > r2:
#                 k = 0
#             else:
#                 k = min(d2[l2 + r2 - i + 1], r2 - i + 1)

#             while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
#                 k += 1

#             d2[i] = k
#             if i + k - 1 > r2:
#                 l2 = i - k
#                 r2 = i + k - 1

#         return d1, d2
