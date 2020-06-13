import utils


if __name__ == "__main__":
  secret = input("Enter your secret (max 50 ascii char): ")
  n = int(input("Enter the key count: "))
  t = int(input("Enter the key count treshold: "))

  secret_int = utils.convert_bytes_to_int(secret.encode('utf-8'))
  shards = utils.generate_shards(secret_int, n, t)
  print("Generated shards:")
  for shard in shards:
    print(f'{shard[0]}-{shard[1]}')