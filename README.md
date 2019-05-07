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
- https://github.com/jereneal20/TIL/blob/master/ps/find-common-characters.cpp
- collections.Counter에 + - & | 연산이 있다. (https://excelsior-cjh.tistory.com/94)
  - 시간복잡도는... 음.... 특성상 O(N) 이겠고, 이걸 string 개수만큼 반복했으니 O(MN) 이렷다. 더 줄일 순 없겠지.

```
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
        
```
- 혹은 map에 단어별 개수를 저장해서 점점 필요한것만 남겨나가는 식으로 할 수 있음.

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
  - 심플한 문제다..만 헤매는..  해쉬테이블을 쓰면 아주 간단하다. 괜히 소팅이나 그런거 고민하지 말자.

- https://leetcode.com/problems/minimum-depth-of-binary-tree
- https://github.com/jereneal20/TIL/blob/master/ps/minimum-depth-of-binary-tree.cpp
  - 복잡도 O(n)
  - Iteration을 도는 방법도 있고 (DFS), BFS 방법도 있다. BFS는 단점도 추가로 있으나 (space) 특성에 따라 빠르게 찾을수도 있다.

## Day 14
- https://leetcode.com/problems/cousins-in-binary-tree
- https://github.com/jereneal20/TIL/blob/master/ps/cousins-in-binary-tree.cpp
  - 두개의 parent가 같은지 보면서 depth가 같은지도 보면 된다.

## Day 15
- https://leetcode.com/problems/generate-parentheses
- https://github.com/jereneal20/TIL/blob/master/ps/generate-parentheses.cpp
  - Backtracking을 하되 branch&bound가 중요하다. 더이상 열려있는게 없을때 더 닫지 않도록, 여는 개수가 일정 수를 초과하지 않도록. 괄호의 종류가 하나기 때문에 이것만 고려해주면 순탄하게 문제 해결 가능.

## Day 17
- https://leetcode.com/problems/add-two-numbers
- https://github.com/jereneal20/TIL/blob/master/ps/add-two-numbers.cpp
  - 자주 풀어야만 했던 문제. 직접 풀었는데 버그가 있다 ㅎㅎ 한방에 통과 좀 하자...

- https://leetcode.com/problems/unique-email-addresses/
- https://github.com/jereneal20/TIL/blob/master/ps/unique-email-addresses.cpp
  - 이건 그래도 한방에 통과. undordered_map이나 set 관련 자료구조를 썼으면 더 좋았을 듯.

## Day 18
- https://leetcode.com/problems/range-sum-query-2d-immutable
- https://github.com/jereneal20/TIL/blob/master/ps/range-sum-query-2d-immutable.cpp
  - DP로 풀어야되는 것은 바로 생각이 났으나, cpp compilation 에러와 소소한 index-1(row1,col1도 덧셈에 포함되는 영역이므로)을 빼먹었다. 컴파일 에러는 call by ref에 의한 것인데, 잘 안쓰는거라 왤까 고민 중...
    - Constructor에서는 const 없이 &로 call by ref를 할 수 없는듯. 구조체에서 생각지 못하게 original value의 값을 바꾸는걸 막기 위한 것 아닐까.

## Day 19
- https://leetcode.com/problems/letter-combinations-of-a-phone-number
  - medium 치고 너무 가볍게 풀 수 있는 문제. 재귀나 loop로 풀면 된다.

## Day 20
- https://leetcode.com/problems/island-perimeter
- https://github.com/jereneal20/TIL/blob/master/ps/island-perimeter.cpp
  - 그냥 카운팅만 하면 되는 문제. 다른 medium 문제들도 도전했으나, 답을 보고야 말았어서 오늘 말고 다른날 재도전하는걸로..

## Day 21
- https://leetcode.com/problems/maximum-subarray
- https://github.com/jereneal20/TIL/blob/master/ps/maximum-subarray.cpp
  - easy 주제에 생각할게 있는 문제. 점화식으로 접근해야 쉽게 풀 수 있다.
  - divide and conquer로는 상당히 어렵다. 절반들의 maximum으로부터 새 maximum을 구하기 위해 필요한 것들이 무엇일까 잘 생각해보아야 함.. 시간이 지나면 또 까먹고 못풀게되지 않을까;

## Day 22
- https://leetcode.com/problems/middle-of-the-linked-list
- https://github.com/jereneal20/TIL/blob/master/ps/middle-of-the-linked-list.cpp
  - 심플한 문제. 토끼와 거북이.

- https://leetcode.com/problems/di-string-match/
- https://github.com/jereneal20/TIL/blob/master/ps/di-string-match.cpp
  - 살짝 고민을 하긴 했는데, 문제가 약간 답정너 같은 느낌으로 쉬운 방식으로 강제될 것 같다고 생각해서 그리디하게 생각해보니 해결.

- https://leetcode.com/problems/flipping-an-image
  - 매우 쉬움. 그냥 단순 구현

## Day 23
- https://leetcode.com/problems/game-of-life
- https://github.com/jereneal20/TIL/blob/master/ps/game-of-life.cpp
  - int variable의 여분을 활용하는 아이디어면 되는 문제. 단, 코드가 지저분해지는걸 어떻게 방지할까..의 문제가...

## Day 24
- https://leetcode.com/problems/flatten-nested-list-iterator/
- https://github.com/jereneal20/TIL/blob/master/ps/flatten-nested-list-iterator.cpp
  - Backtracking 방식으로 순회하는 로직을 구현하는 문제. Iterator를 잘 쓸 수 있으면 훨씬 쉬운데, 그렇지 못해서 코드를 엉망진창으로 짜다 겨우 완성..

## Day 25
- https://leetcode.com/problems/binary-search-tree-iterator
- https://github.com/jereneal20/TIL/blob/master/ps/binary-search-tree-iterator.cpp
  - 상대적으로 만만한 medium 문제였음. DFS를 재귀 대신 class 내에서 컨트롤 할 수 있도록 하면 됐기 때문에, stack을 쓰는 것으로 해결 가능했음.

## Day 26
- https://leetcode.com/problems/powx-n
- https://github.com/jereneal20/TIL/blob/master/ps/powx-n.cpp
  - 질문 받은적 있는 문제 유형이라 쉽게 풀었다. DP 느낌으로 하긴 했는데, 사실 그냥 저장하지말고 바로 곱셈을 진행해버려도 된다. 공짜 medium 문제.

## Day 27
- https://leetcode.com/problems/merge-sorted-array
- https://github.com/jereneal20/TIL/blob/master/ps/merge-sorted-array.cpp
  - 두개의 배열을 이미 있는 배열에 합치는거라 순간 흠칫했다. 빈공간부터 채워가면 되는거였는데.. 이런 아이디어 좀 잘 생각났으면..

## Day 28
- https://leetcode.com/problems/best-sightseeing-pair/
- https://github.com/jereneal20/TIL/blob/master/ps/best-sightseeing-pair.cpp
  - 처음엔 좀 헤매다가 살짝 답안의 타이틀들을 보고 솔루션이 떠오른. 기존에 이런 문제 많은데 그걸 떠올리지 못하니 문제...

## Day 29
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock
- https://github.com/jereneal20/TIL/blob/master/ps/best-time-to-buy-and-sell-stock.cpp
  - 28일에 푼 문제와 비슷한 유형의 문제. 이거 시리즈로 몇개 있는데 쭉 풀어봐야겠다.

## Day 30
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
- https://github.com/jereneal20/TIL/blob/master/ps/best-time-to-buy-and-sell-stock-ii.cpp
  - 이건 어이가 없을 정도로 더 쉬워졌다. increasing 하는 곳들의 합을 구하면 끝.

## Day 31
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
- https://github.com/jereneal20/TIL/blob/master/ps/best-time-to-buy-and-sell-stock-with-cooldown.cpp
  - 이 문제는 좀 어려워졌다. DP문제는 확실한데 판 직후에 사면 안된다는 점이 까다롭다. state로 각 state에 최대값을 업데이트 해내는 형태로 가능했다.

## Day 32
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
- https://github.com/jereneal20/TIL/blob/master/ps/best-time-to-buy-and-sell-stock-with-transaction-fee.cpp
  - 어제 푼 문제와 유사하다. 오히려 더 쉬워진 느낌. 반복학습의 효과인가...

## Day 33
- https://leetcode.com/problems/ugly-number
- https://leetcode.com/problems/sort-array-by-parity-ii
  - 누군가 풀었던 두 문제. 기본적인 느낌의 문제들

## Day 34
- https://leetcode.com/problems/maximum-swap
- https://github.com/jereneal20/TIL/blob/master/ps/maximum-swap.cpp
  - 나중에 다시 풀어보는게 좋을 것 같다. 해설은 코드에 주석으로 써뒀다. 

## Day 35
- https://leetcode.com/problems/next-greater-node-in-linked-list
- https://github.com/jereneal20/TIL/blob/master/ps/next-greater-node-in-linked-list.cpp
  - 스택을 이용하면 된다. 고민끝에 생각해내서 다행..

## Day 36
- https://leetcode.com/problems/create-maximum-number
- https://github.com/jereneal20/TIL/blob/master/ps/create-maximum-number.cpp
  - 약간 느린 solution으로 풀었다. 최적화를 더 할 수 있다.
  - 현재 시간복잡도는 각각의 길이를 N, M이라 할 때 `O(k*(N+M)^2)` 이다. `O(k*(N+M))`으로 줄일 수 있다는데.. suffix array를 참고하라고한다.
    - https://web.archive.org/web/20160120093629/http://algobox.org/create-maximum-number/

## Day 37
- https://leetcode.com/problems/remove-k-digits
- https://github.com/jereneal20/TIL/blob/master/ps/remove-k-digits.cpp
  - 앞선 문제의 축소판. 예외처리에 좀 더 신경써서 문제를 풀자. 간단하니 차후에 다시 풀어봐도 좋다.

## Day 38
- https://leetcode.com/problems/daily-temperatures
- https://github.com/jereneal20/TIL/blob/master/ps/daily-temperatures.cpp
  - 위 문제들과 동일한 유형의 문제

## Day 39
- https://leetcode.com/problems/perfect-squares
- https://github.com/jereneal20/TIL/blob/master/ps/perfect-squares.cpp
  - 답지를 참고했어서 다시한번 생각해봐야한다.

## Day 40
- https://leetcode.com/problems/k-closest-points-to-origin
- https://github.com/jereneal20/TIL/blob/master/ps/k-closest-points-to-origin.cpp
  - 알고 있던 솔루션으로는 풀었는데 답지를 보니 더 좋은 솔루션이 있다.. 이걸 추가로 공부해야할듯.

## Day 41
- 39일자의 문제를 BFS with B&B로 풀었다. 수학으로 푸는 방법은 라그랑주의 네수 정리에 의한 것이었다...

##  Day42
- https://leetcode.com/problems/longest-palindromic-substring
- https://github.com/jereneal20/TIL/blob/master/ps/longest-palindromic-substring.cpp
  - 이전에 봤던 솔루션을 기억해내 풀었다. 조금 더 효율적인 솔루션도 있어서 다시 풀어봐야한다.

## Day 43
- Day 40의 N 솔루션이 있다는 말은 사실 사기였다. N^2인데 best case에 N이 가능한 솔루션이었을 뿐. 퀵소트의 left right를 가르는 로직을 이용하면 된다는 논지인데, 구현해보는건 좋을 것 같긴하다. 동시에 퀵소트 구현도 한번....

## Day 44
- 이래도 되는걸까 싶을정도로 쉬운 문제 2개 풂. 하지만 모음에는 소문자 모음 뿐만 아니라 대문자 모음도 있다는 사실을 간과함..

## Day 45
- 노동자의 날이니 쉬어가는 차원에서 지금까지 어떤 문제들을 풀었는지 간략하게 살펴봄. medium 문제들을 더 풀고 열어두고 해결 못한 leetcode 페이지들을 이해하고 꺼야하는데.. 하는 생각만 반복합니다.

## Day 46
- https://leetcode.com/problems/next-greater-element-ii
- https://github.com/jereneal20/TIL/blob/master/ps/next-greater-element-ii.cpp
  - 얼마전에 푼 이와 비슷한 문제와 동일한 유형. circular 이기 때문에 최대 2번 루프를 돈다는 아이디어만 있으면 된다.

## Day 47
- https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
- https://github.com/jereneal20/TIL/blob/master/ps/minimum-add-to-make-parentheses-valid.cpp
  - 맨날 면접문제로 내던 문제의 약 변형 문제라 어렵지 않게 풀 수 있었다.

- https://leetcode.com/problems/check-if-word-is-valid-after-substitutions
  - Pumping lemma를 생각나게하는 문제. 안에서 반복되지 않는 string이 솟아나는(?)거라 결국 위에 문제랑 같다. 다만 이 경우는 (가 a일수도, ab일수도 있으므로 스택 사용이 필수적이 된다.

## Day 48
- https://leetcode.com/problems/vowel-spellchecker
  - TLE가 나오는 solution. 더 빠른 솔루션을 보고 개선해야한다. 공부할 여지가 있어 좋은 문제

## Day 49
- 어제 문제 다시 풂. 시간복잡도는 줄어들지 않지만 최적화를 더 하면 되는거였음. 시간복잡도도 줄일 수 있는데, 각 조건에 대해 각각 배열을 만들고 어차피 가장 첫번째것만 쓰기 때문에 그거만 저장하는 것으로 가능.

## Day 50
- https://leetcode.com/problems/3sum/
  - 이 솔루션으로는 안된다. 두개의 index를 l r에서 중앙으로 오면서 값을 찾는 로직으로 풀 수 있는데, 왜그게 특정 값 x를 찾아낼 수 있는지 모르겠다. 고민중...

## Day 51
- 50일차 문제를 풀었음. 뭔가 다른 사람에게 설명하긴 좀 껄끄럽지만, 여하튼 이해하고 코드로 구현은 완료.
