# -*- coding: utf-8 -*-
# file: pygraph.py
#
def searchGraph(graph, start, end):
	results = []
	generatePath(graph, [start], end, results)
	results.sort(key=lambda x: len(x))
	return results
def generatePath(graph, path, end, results):
	state = path[-1]
	if state == end:
		results.append(path)
	else:
		for arc in graph[state]:
			if arc not in path:
				generatePath(graph, path + [arc], end, results)
if __name__ == '__main__':
	Graph = {'A': 	['B', 'C', 'D'],
			'B':	['E'],
			'C':	['D', 'F'],
			'D':	['B', 'E', 'G'],
			'E':	[],
			'F':	['D', 'G'],
			'G':	['E']}
	r = searchGraph(Graph, 'A', 'D')
	print '*' * 30
	print '	path A to D '
	print '*' * 30
	for i in r:
		print i
	r = searchGraph(Graph, 'A', 'E')
	print '*' * 30
	print 'path A to E'
	print '*' * 30
	for i in r:
		print i
	r = searchGraph(Graph, 'C', 'E')
	print '*' * 30
	print 'path C to E'
	print '*' * 30
	for i in r:
		print i