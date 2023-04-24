import redis
from config.yaml_config import GetConfig


class RedisOperation(object):
    def __init__(self):
        redis_info = GetConfig().get_redis()
        self.redis_client = redis.Redis(
            host=redis_info["host"],
            port=redis_info["port"],
            db=redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding="UTF-8"
        )


if __name__ == '__main__':
    print(RedisOperation().redis_client.get('yangyang'))
