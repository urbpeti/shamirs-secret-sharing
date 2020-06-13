import unittest
from unittest.mock import patch
import utils

class TestUtils(unittest.TestCase):
  def test_convert_bytes_to_int(self):
    cases = [
      (b'a', 97),
      (b'ab', 24930),
      (b'AZ', 16730),
    ]
    for case in cases:
      self.assertEquals(utils.convert_bytes_to_int(case[0]), case[1])

  def test_convert_int_to_bytes(self):
    cases = [
      (b'a', 97),
      (b'ab', 24930),
      (b'AZ', 16730),
    ]
    for case in cases:
      self.assertEquals(utils.convert_int_to_bytes(case[1]), case[0])
    
  def test_evaluate_polynom(self):
    cases = [
      ([3], 0, 7, 3),
      ([3, 1], 1, 7, (3 + 1 * 1) % 7),
      ([3, 1], 2, 7, (3 + 1 * 2) % 7),
      ([1, 2], 2, 7, (1 + 2 * 2) % 7),
      ([3, 2], 2, 7, (3 + 2 * 2) % 7),
      ([3, 2, 5], 3, 17, (3 + 2 * 3 + 5 * 3 * 3) % 17),
    ]
    for case in cases:
      self.assertEquals(utils.evaluate_polynom(case[0], case[1], case[2]), case[3])
    
  def test_generate_shards_should_return_the_secret_when_the_key_threshold_is_one(self):
    secret = 4
    self.assertEquals(utils.generate_shards(secret, 1, 1, P=7), [(1, hex(4))])

  def test_generate_shards_should_create_shards_equals_to_key_numbers(self):
    secret = 4
    self.assertEquals(utils.generate_shards(secret, 2, 1, P=7), [(1, hex(4)), (2, hex(4))])

  @patch('utils.randint')
  def test_generate_shards(self, randint):
    randint.return_value = 5
    secret = 4
    self.assertEquals(utils.generate_shards(secret, 3, 2, P=7),
      [
        (1, hex(2)),
        (2, hex(0)),
        (3, hex(5)),
      ]
    )

  def test_retrieve_secret_int_all_key(self):
    shards = [
        (1, hex(2)),
        (2, hex(0)),
        (3, hex(5)),
      ]
    self.assertEquals(utils.retrieve_secret_int(shards, P=7), 4)

  def test_retrieve_secret_int_with_treshold_key_count(self):
    shards = [
        (1, hex(2)),
        (3, hex(5)),
      ]
    self.assertEquals(utils.retrieve_secret_int(shards, P=7), 4)