# TIL
Today I Learn

## Day 1
- 타노스 장애 처리를 하다보니 알던 것도 다시 검색하고 있는 자신을 발견하게 됨.
  - `ps -aef | grep server | grep -v grep`
    - 자기 자신을 grep 결과에서 빼고 싶을 때...
  - `cat file | sed -e 's/^/prefix/' > new_file`
    - prefix를 매 라인마다 앞에 넣고 싶을 때...
  - `for i in {1..10}; do sth; done` 을 ctrl+z; bg를 하면 지금까지 진행 중인 sth만 수행하고 종료된다. 끝까지 실행하고 싶으면 이 명령을 파일로 옮겨서 실행해야 함.

## Day 2
- Stderr/Stdout 이 출력되는 프로세스를 ctrl+z 후 bg를 하면 예외처리를 하지 않는 이상 에러를 뿜고 프로세스가 죽는다.
  - `CMD > /dev/null 2>&1` 을 뒤에 붙여 프로세스를 수행하도록 하자

## Day 3
- Ansible tip
  - 옛날 버전: `ansible -i <server_list> -m shell -a "ls" -f 10 tset-sa[!1-3]-9[!0-9]`
  - 최근 버전: `ansible -i <server_list> -m shell -a "ls" -f 10 ~tset-sa[1-3]-9[0-9]$`
  - 옛날 버전은 자동으로 regex를 적용시켜 줬지만, 최근 버전은 `~`를 명시해야 regex를 적용시켜준다. 이게 없으면 <server_list>의 몇번째 매칭된 파일인지.. 등과 같은 형태로 패턴을 찾는다.
  - https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html#intro-patterns
    - 이걸 끝까지 안 읽어서 맨날 헤맸다.. 
    - Most people don’t specify patterns as regular expressions, but you can. Just start the pattern with a ‘~’

## Day 4
- https://leetcode.com/problems/find-common-characters/
- collections.Counter에 + - & | 연산이 있다. (https://excelsior-cjh.tistory.com/94)
  - 시간복잡도는... 음.... 특성상 O(N) 이겠고, 이걸 string 개수만큼 반복했으니 O(M*N) 이렷다. 더 줄일 순 없겠지.

```
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
        
```

## Day 5
- https://leetcode.com/problems/odd-even-linked-list/
- https://github.com/jereneal20/TIL/ps/odd-even-linked-list.cpp
  - Complexity: time O(N), space O(1)
  - 홀짝 구별이기 때문에 iterator variable i를 두고 홀짝일때 각각 홀짝 ListNode에 해당 Node를 append 시킨다. cur가 지나간 것들만 inplace 하므로 iteration에 문제가 생기진 않음. 마지막 even node->next에 명시적으로 NULL을 넣어주자.

