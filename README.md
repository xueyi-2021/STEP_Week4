

# STEP WEEK4 Homework

## DFSとBFSで経路を探す



### 方針

- 辞書pages_visitedを利用して訪問したページを記録して無限ループが発生しないようにする

- 辞書distanceを使って、このページから次のページを訪問する時：

  - ```
    次のページのdistance = このページのdistance+1
    ```

- 辞書parentを使って、このページから次のページを訪問する時：

  - ```
    次のページの親 = このページ
    ```

  - ような形で経路を復元したいと思っている

<br>

### 出力

- Googleから渋谷まで辿れるかどうか、経路の長さ、経路の3つの結果を出力する

#### BFS(幅優先探索)

- 「Google」から「渋谷」に辿れる
  - 距離は2
  - 経路は「Google」→「フジテレビジョン」→「渋谷」
- 「Google」から一番遠いページは「ハンティントン駅」、距離は16

#### DFS(深さ優先探索)(スタック)

- 「Google」から「渋谷」に辿れる、経路の長さ毎回違う（なぜ毎回違うんだろう……）
- 「Google」から一番遠いページも不特定、長さ大体50000超える

<br>

[^]: DFSの再帰バージョンまだデバッグ中……

<br>

### 実行環境

- python3.6以上
