import os, sys, unittest

sys.path.insert(0, os.path.dirname(__file__))
from assemble import rank

HIGH, MID, LOW = 0.9, 0.5, 0.2


def findings(*rels):
    return [{'relevance': r} for r in rels]


class RankTest(unittest.TestCase):
    def test_orders_by_best_finding_relevance(self):
        papers = {'a': findings(LOW), 'b': findings(HIGH), 'c': findings(MID)}
        self.assertEqual(rank(list(papers), papers.get), ['b', 'c', 'a'])

    def test_ties_on_best_broken_by_mean(self):
        papers = {'thin': findings(HIGH, LOW), 'dense': findings(HIGH, MID)}
        self.assertEqual(rank(list(papers), papers.get), ['dense', 'thin'])

    def test_full_ties_keep_given_order(self):
        papers = {'first': findings(MID), 'second': findings(MID)}
        self.assertEqual(rank(['first', 'second'], papers.get), ['first', 'second'])
        self.assertEqual(rank(['second', 'first'], papers.get), ['second', 'first'])

    def test_relevance_given_as_string(self):
        papers = {'s': [{'relevance': '0.3'}], 'n': findings(MID)}
        self.assertEqual(rank(list(papers), papers.get), ['n', 's'])


if __name__ == '__main__':
    unittest.main()
