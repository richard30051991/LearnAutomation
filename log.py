import argparse
import re
import json
from collections import defaultdict
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Process access.log')
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/library/argparse.html#the-add-argument-method
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()


def parser_log(file):
    dict_method = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0, "CONNECT": 0, "OPTIONS": 0, "TRACE": 0}
    ip_method = defaultdict(lambda: {})
    general_dict = {
        "top_ips": {},
        "top_longest": [
            {
                "ip": "",
                "date": "",
                "method": "",
                "url": "",
                "duration": 0
            },
            {
                "ip": "",
                "date": "",
                "method": "",
                "url": "",
                "duration": 0
            },
            {
                "ip": "",
                "date": "",
                "method": "",
                "url": "",
                "duration": 0
            }
        ],
        "total_stat": {},
        "total_requests": 0
    }
    idx = 0
    for line in file:
        if idx > 99:
            break
        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match is not None:
            ip = ip_match.group()
            if ip in ip_method:
                ip_method[ip] += 1
            else:
                ip_method[ip] = 1

        method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line)
        if method is not None:
            method_x = method.group(1)
            dict_method[method_x] += 1

        longest = re.split(r'["]', line)
        if int(longest[6]) >= general_dict["top_longest"][0]["duration"]:
            general_dict["top_longest"][0]["ip"] = ip
            general_dict["top_longest"][0]["date"] = longest[0].split("- ")[2]
            general_dict["top_longest"][0]["method"] = longest[1].split()[0]
            general_dict["top_longest"][0]["url"] = longest[3]
            general_dict["top_longest"][0]["duration"] = int(longest[6])
        elif int(longest[6]) >= general_dict["top_longest"][1]["duration"]:
            general_dict["top_longest"][1]["ip"] = ip
            general_dict["top_longest"][1]["date"] = longest[0].split("- ")[2]
            general_dict["top_longest"][1]["method"] = longest[1].split()[0]
            general_dict["top_longest"][1]["url"] = longest[3]
            general_dict["top_longest"][1]["duration"] = int(longest[6])
        elif int(longest[6]) >= general_dict["top_longest"][2]["duration"]:
            general_dict["top_longest"][2]["ip"] = ip
            general_dict["top_longest"][2]["date"] = longest[0].split("- ")[2]
            general_dict["top_longest"][2]["method"] = longest[1].split()[0]
            general_dict["top_longest"][2]["url"] = longest[3]
            general_dict["top_longest"][2]["duration"] = int(longest[6])

        idx += 1

    ip_method = dict(sorted(ip_method.items(), key=lambda x: x[1], reverse=True))
    total_requests = sum(dict_method.values())
    keys = list(ip_method.keys())

    for i in range(0, 3):
        general_dict["top_ips"][keys[i]] = ip_method[keys[i]]
    general_dict["total_stat"] = dict_method
    general_dict["total_requests"] = total_requests
    print(json.dumps(general_dict, indent=4))


if os.path.isfile(args.file):
    if Path(args.file).stat().st_size > 0:
        print("Логи по файлу", args.file)
        with open(args.file) as file:
            parser_log(file)
    else:
        print(f"Файл '{args.file}' пуст")

elif os.path.isdir(args.file):
    if len(os.listdir(args.file)) >= 1:
        for filename in os.listdir(args.file):
            path_file = os.path.join(args.file, filename)
            if Path(path_file).stat().st_size > 0:
                print("Логи по файлу", path_file)
                with open(os.path.join(args.file, filename)) as file:
                    parser_log(file)
            else:
                print(f"Файл '{path_file}' пуст")
    else:
        print("Директория пуста")


