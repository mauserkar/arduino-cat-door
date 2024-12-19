import cats_door.logger as logger


def parse_request_to_dict(request):
    result = {}
    for line in request.splitlines():
        logger.info(f"line: {line}")
        if line:
            if line.startswith("request:"):
                key, value = line.split(": ", 1)
                result = {key: value}
    return result
