import re
import datetime as dt
import subprocess


def main():
    file_path = "/opt/minecraft-server/logs/latest.log"
    # split_pattern = re.compile(r"(\d{2}\w{3}\d{4}\s\d{2}:\d{2}:\d{2}.\d{3}).*?\:\s(.*)")
    split_pattern = re.compile(r"(\d{2}:\d{2}:\d{2}).*?\:\s(.*)")
    # datetime_format = "%d%b%Y %H:%M:%S.%f"
    # datetime_format = "%H:%M:%S"

    # now_utc = dt.datetime.now(dt.timezone.utc)
    # logs = []

    with open(file_path, "r", encoding="utf8") as f:
        # first_log = split_pattern.findall(line)[0]
        # first_log_time = dt.datetime.strptime(first_log[0], datetime_format).astimezone(
        #     dt.timezone.utc
        # )
        # if now_utc - first_log_time <= dt.timedelta(minutes=15):
        #     print("starting")
        #     return

        lines = f.read().splitlines()
        lines_splitted = [split_pattern.findall(line)[0] for line in lines]
        # logs = [
        #     (
        #         dt.datetime.strptime(dt_str, datetime_format).astimezone(
        #             dt.timezone.utc
        #         ),
        #         message,
        #     )
        #     for dt_str, message in lines_splitted
        # ]
        logs = [message for dt_str, message in lines_splitted]

    login_pattern = re.compile(r"joined the game")
    # login_count = len([1 for _, message in logs if login_pattern.search(message)])
    login_count = len([1 for message in logs if login_pattern.search(message)])
    logout_pattern = re.compile(r"left the game")
    # logout_count = len([1 for _, message in logs if logout_pattern.search(message)])
    logout_count = len([1 for message in logs if logout_pattern.search(message)])

    if login_count <= logout_count:
        print("shutdown")
        # subprocess.run(["sudo", "shutdown", "-h", "now"], check=False)
        return

    print("someone is login")


if __name__ == "__main__":
    main()