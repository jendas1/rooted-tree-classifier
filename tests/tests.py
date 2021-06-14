#!/usr/bin/python3

import unittest, subprocess, sys
from io import StringIO
from unittest.mock import patch

from rooted_tree_classifier import decide_complexity

class TestE2E(unittest.TestCase):
  def testDeciderProblem1(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"111", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "O(1)")
    self.assertEqual(lines[1], "")

  def testDeciderProblem2(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"121 123 212 131 323 454", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "Θ(log*n)")
    self.assertEqual(lines[1], "")

  def testDeciderProblem3(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"454", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "unsolvable")
    self.assertEqual(lines[1], "")

  def testDeciderProblem4(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"1M1 010 M11 M01", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "O(1)")
    self.assertEqual(lines[1], "")

  def testDeciderProblem5(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"121 112 212", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "Θ(log n)")
    self.assertEqual(lines[1], "")

  def testDeciderProblem6(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"212 122 111", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "O(1)")
    self.assertEqual(lines[1], "")

  def testDeciderProblem7(self):
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        decide_complexity("212 313 323 131 1x1 xx1".split())
        self.assertEqual(fakeOutput.getvalue().strip(), 'Θ(log*n)')

  # (1:22)
  # (1:2x)
  # (1:xx)
  # (2:11)
  # (2:1x)
  # (2:xx)
  # (x:1a)
  # (x:2a)
  # (x:xa)
  # (x:aa)
  # (a:bb)
  # (b:aa)
  def testDeciderProblem8(self):
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        decide_complexity("212 21x x1x 121 12x x2x 1xa 2xa axa bab aba".split())
        self.assertEqual(fakeOutput.getvalue().strip(), 'Θ(n^(1/2))')

  def testDeciderProblem9(self):
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        decide_complexity("212 121 12x 1xa bab aba".split())
        self.assertEqual(fakeOutput.getvalue().strip(), 'Θ(n^(1/2))')

  def testDecider1(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"111", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "O(1)")
    self.assertEqual(lines[1], "")

  def testDecider2(self):
    result = subprocess.run([sys.executable, '-m', 'rooted_tree_classifier'], input=b"121 212", capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "Θ(n)")
    self.assertEqual(lines[1], "")


