import collections
import networkx as nx

def bfs(pages, links, start, target):
  container = collections.deque()
  pages_visited = {}

  container.append(start)
  pages_visited[start] = 1

  #startからの距離を記録する
  distance = {}
  distance[pages[start]] = 0

  #親のページを記録する
  parent = {}
  parent[pages[start]] = None

  while (len(container) > 0):
    node = container.popleft()
    #if node == target:
    #  return True

    for linked_page in links[node]:
      if linked_page not in pages_visited:
        #print("children:", linked_page, pages[linked_page])
        container.append(linked_page)
        pages_visited[linked_page] = 1
        distance[pages[linked_page]] = distance[pages[node]] + 1
        parent[pages[linked_page]] = pages[node]

  return distance, parent


def dfs_stack(pages, links, start, target):
  container = collections.deque()
  pages_visited = {}

  container.append(start)
  pages_visited[start] = 1

  #訪問順(?)を確認する用
  list_visted = []

  distance = {}
  distance[pages[start]] = 0

  parent = {}
  parent[pages[start]] = None

  while (len(container) > 0):
    node = container.pop()
    list_visted.append(pages[node])
    #if node == target:
    #  return True

    for linked_page in links[node]:
      if linked_page not in pages_visited:
        #print("children", linked_page, pages[linked_page])
        container.append(linked_page)
        pages_visited[linked_page] = 1
        distance[pages[linked_page]] = distance[pages[node]] + 1
        parent[pages[linked_page]] = pages[node]

  return distance, parent


def find_furthest_page(distance):
  #最も遠いページを探す
  max_dis = -1
  for name, dis in distance.items():
    if dis > max_dis:
      max_dis = dis
  max_names = []
  for name, dis in distance.items():
    if dis == max_dis:
      max_names.append(name)

  #print(max_names, max_dis)
  return max_names, max_dis


def find_path(pages, parent, start, target):
  node = pages[target]
  path = [node]
  while parent[node] != None:
    path.insert(0, parent[node])
    node = parent[node]
  return path

def check(pages, start, target, distance):
  if pages[target] in distance:
    print(pages[target], "is found, the length of path from", pages[start], "is", distance[pages[target]])
  else:
    print(pages[target], "is not found")
  return


def main():
  pages = {}
  links = {}

  #ちなみにサンプルコードにencoding="utf-8"がないのでエラーが出る
  #with open('data/pages_small.txt', encoding="utf-8") as f:
  with open('data/pages.txt', encoding="utf-8") as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  #with open('data/links_small.txt', encoding="utf-8") as f:
  with open('data/links.txt', encoding="utf-8") as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}

  #links.txtに出現しないページのlinksも作る（隣接リストを完成させるみたいに）
  for k, v in pages.items():
    if k not in links:
      links[k] = {}

  #探索の起点と終点を定義する
  for k, v in pages.items():
    if v == 'Google':
      start = k
    if v == '渋谷':
      target = k


  print("BFS:")
  bfs_distance, bfs_parent = bfs(pages, links, start, target)
  bfs_max_pages, bfs_max_distance = find_furthest_page(bfs_distance)
  check(pages, start, target, bfs_distance)
  bfs_path = find_path(pages, bfs_parent, start, target)
  print("The path is", bfs_path)


  print("DFS(stack):")
  dfs_distance, dfs_parent = dfs_stack(pages, links, start, target)
  dfs_max_pages, dfs_max_distance = find_furthest_page(dfs_distance)
  check(pages, start, target, dfs_distance)
  dfs_path = find_path(pages, dfs_parent, start, target)
  print("The path is", dfs_path)


  '''
  #小さいグラフだけ対応できるようです、、、
  nx_graph1 = nx.DiGraph()
  for node1, linked_pages in links.items():
    for node2 in linked_pages:
      nx_graph1.add_edge(pages[node1], pages[node2])

  for path in nx.all_simple_paths(nx_graph1, source='Google', target='ゲーム'):
      print(len(path), path)
  '''

if __name__ == '__main__':
  main()