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
- https://github.com/jereneal20/TIL/blob/master/ps/odd-even-linked-list.cpp
  - Complexity: time O(N), space O(1)
  - 홀짝 구별이기 때문에 iterator variable i를 두고 홀짝일때 각각 홀짝 ListNode에 해당 Node를 append 시킨다. cur가 지나간 것들만 inplace 하므로 iteration에 문제가 생기진 않음. 마지막 even node->next에 명시적으로 NULL을 넣어주자.

## Day 6
- https://leetcode.com/problems/add-strings
- https://github.com/jereneal20/TIL/blob/master/ps/odd-even-linked-list.cpp
  - 평소때 하던 로직대로 짜면 된다. Carry 마지막 처리와 index 에러 처리에 주의하며 프로그래밍하면 된다. 이런건 더 빠르게 짤 수 있어야 하는데...

## Day 7
- C++의 unordered_map과 map의 차이
  - https://a.cyclic.dev/day05/ 를 보다가, map이 왜 tree로 만들어져있지?! 띠잉 하고 이것저것 뒤적여봤다. 결론은 ordered_map이 map인 셈... 요즘 cpp를 문제 푸는 용도로만 쓰다보니 그냥 무작정 unordered_map만 써대서 생각도 깊이 안 해봤었다.
  - [차이 설명 링크](http://lab.gamecodi.com/board/zboard.php?id=GAMECODILAB_QnA_etc&no=3392) 여기 설명이 명확하다. 결론적으로 트리구조 자료 저장 방식과 맵 구조 자료 저장 방식의 차이를 이야기해준다.
  - [GeeksForGeeks](https://www.geeksforgeeks.org/map-vs-unordered_map-c/) 여기 요약도 명료하다. 순서나 range가 필요한 경우, skewed된 경우, 등등... 은 map이 유리.
  - 반대로 말하면 tree 구조를 사용해야 할 때 map을 사용하면 편할 것 같다. 문제 풀 때 이런 일이 있으면 꼭 써보자.
  
## Day 8
- https://leetcode.com/problems/bitwise-and-of-numbers-range/
- https://github.com/jereneal20/TIL/blob/master/ps/bitwise-and-of-numbers-range.cpp
  - 복잡도 O(1)
  - 구간에 대해 모두 and operation을 취하기 때문에 특정 bit가 달라지는 시점부터는 무조건 하위 bit는 0이 된다. n >= m 이므로 어떤 bit들까지는 모두 같다가 어디선가 달라지는데 (leading zero 포함), 그 bit에서 n은 1이고, m은 0일 것이다. 이는 range 내에 그 하위의 1111과 같이 최대값이 포함되고, 그 다음 10000과 같이 0으로 set된 값이 포함되기 마련이므로 하위 비트는 and에서 무시하여도 됨.

## Day 9
- https://leetcode.com/problems/sum-of-left-leaves/
- https://github.com/jereneal20/TIL/blob/master/ps/sum-of-left-leaves.cpp
  - 복잡도 O(n)
  - left leaves만 찾으면 되는데, 이 leaf가 left에서 끝나는 것인지를 알려면 그 parent에서 검색해야함. 

## Day 10
- https://leetcode.com/problems/rotate-function
- https://github.com/jereneal20/TIL/blob/master/ps/rotate-function.cpp
  - 복잡도 O(n)
  - 곱셈이 순차적으로 일어나기 때문에 하나의 답을 구한 후 한번의 연산으로 그다음 답을 구할 수 있다.

- Integer promotion 버그
  - vector의 size를 구하면 이는 signed type의 값이다. 이때, 음수 값과 연산을 진행하는 경우 integer promotion이 발생해 값이 잘못 출력되는 경우가 발생한다.
- 아래 코드의 결과를 예상해보자. -4일까? 아니다. -2가 강제 promotion 되어 양수로 바뀐 상태로 계산을 수행한다.
```
#include <vector>
#include <iostream>
using namespace std;

int main()
{
	vector<int> vec;
	vec.push_back(1);
	vec.push_back(1);

	cout << -2 * vec.size() << endl;
	return 0;
}

```

## Day 11
- https://leetcode.com/problems/longest-common-prefix
- https://github.com/jereneal20/TIL/blob/master/ps/longest-common-prefix.cpp
  - 복잡도 O(n), n은 전체 strs의 chars를 합한 것.
  - 어차피 앞부분은 순회를 해야하므로 n보다 줄어들 수는 없다.
  - 이 코드에도 예외케이스 처리를 좀 덜 해줬는데 accept되는 것이... 일부 string의 길이가 짧을 때 것을 추가 예외처리해줘야한다.

## Day 12
- https://leetcode.com/problems/longest-substring-without-repeating-characters
- https://github.com/jereneal20/TIL/blob/master/ps/longest-substring-without-repeating-characters.cpp
  - 복잡도 O(n)
  - 문제를 잘 읽자. reapeating characters의 정의를 헷갈리니 한참 헤맨다.
  - dict에 넣어서 풀면 된다. unordered_map의 [] operator는 자동으로 element를 생성시켜주니 주의하고, map.find(key)==map.end()를 활용하자. ==이면 element not exist.

## Day 13
- https://leetcode.com/problems/two-sum
- https://github.com/jereneal20/TIL/blob/master/ps/two-sum.cpp
  - 복잡도 O(n)
  - 심플한 문제다..만 헤매는 -_- 해쉬테이블을 쓰면 아주 간단하다. 괜히 소팅이나 그런거 고민하지 말자.
