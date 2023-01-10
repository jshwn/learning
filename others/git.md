#   Git

##  Reference
*   [Visualized Cheatsheet](https://ndpsoftware.com/git-cheatsheet.html#loc=index;)

##  Git Tutorial
ref: [`man gittutorial`](https://git-scm.com/docs/gittutorial)

```sh
git diff --cached
```
`--cached` option을 붙이지 않으면 아직 `add`하지 않은(unstaged) file들까지 모두 출력하게 된다.

Git tracks content not files: Git은 

`git log`에 `-p` 옵션을 붙이면 매 commit마다 complete diffs를 첨부하여 출력한다.

##  Detached Head
ref: https://git-scm.com/docs/git-checkout#_detached_head


##  issues

### git checkout to git switch and git resotre
git checkout은 하나의 command가 너무 많은 기능을 내포하고 있어서 이를 `git switch`와 `git restore`로 분리하였다.

`git checkout -b|B`는 `git switch -c|C`에 대응한다.

### git PR conflict (Can't automatically merge)
*   참고: https://ansohxxn.github.io/git/merge/
*   fast-forward
    *   `git rebase <parent branch>` in target branch
    *   `git merge --ff-only <parent branch>` in target branch

##  Use cases
*   `git commit --amend`: 가장 최근 commit message 수정
*   `git checkout`
    *   GIT-CHECKOUT(1), Git Manual 참고
    *   `-b <branch>`: 
*   `git checkout -- <filename>`: 하나의 file만 직전commit 상태로 reset하기
*   `git checkout .`은 `git reset`과 비슷한 효과
*   `git switch <branch>`: remote branch가 존재할 경우, `git fetch` 후에 사용
    *   ref: https://stackoverflow.com/a/9537923