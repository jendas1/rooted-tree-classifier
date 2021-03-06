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
    self.assertEqual(lines[0], "Ω(n)")
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
    self.assertEqual(lines[0], "Ω(n)")
    self.assertEqual(lines[1], "")


