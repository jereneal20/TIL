class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # 나머지가 0인 경우가 n의 경우의 수 중 하나라도 존재하는 케이스 -> 문제없음
        # 존재하지 않는 케이스 -> 1의 개수가 K개 이상일때까지 수 중 나머지가 같은 경우가 하나 이상은 발생. (나머지로 가능한 건 1~K-1이고, 숫자 개수가 K개 이상이면.)
        # 하나 이상 겹친다면 여긴 사이클이 생기게 됨. 왜냐, 직전 수의 나머지가 다음 수의 나머지를 결정하기 때문. -> next_mod = (10 * prev_mod + 1) % K
        # 왜냐하면 어떤 숫자를 n = kq + r 라 할 때 다음 숫자는 10kq+10r+1이고, 나머지를 구할때 10kq는 나누어 떨어지므로 필요없기 때문.
        # K번까지 0을 만들지 못한 숫자는 불가능하다 보면 됨.
        r = length = 1
        while length <= k:
            r = r % k
            if r == 0: return length
            length += 1
            r = 10 * r + 1
        return -1

        # optimize를 위해 불가능함이 자명한 2 5 케이스를 배제해도 좋음.
