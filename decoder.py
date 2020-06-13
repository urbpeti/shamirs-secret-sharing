import utils

if __name__ == "__main__":
  shards = input("Enter the key shards separated by comma: ").split(',')
  shards = [(int(s.split('-')[0]), hex(int(s.split('-')[1], 16))) for s in shards]
  retrieved_secret_int = utils.retrieve_secret_int(shards)
  print(f'Secret message: {utils.convert_int_to_bytes(retrieved_secret_int)}')