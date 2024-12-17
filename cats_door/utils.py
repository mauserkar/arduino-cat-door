def parse_request_to_dict(request):
    result = {}
    for line in request.splitlines():
        print(f"line: {line}")
        if line:
            if line.startswith("request:"):
                key, value = line.split(": ", 1)
                result = {key: value}
    return result
