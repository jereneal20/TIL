class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))

        # num_list = list(str(num))
        # for idx in range(0, len(num_list)):
        #     if num_list[idx] == '6':
        #         num_list[idx] = '9'
        #         break
        # return int("".join(num_list))