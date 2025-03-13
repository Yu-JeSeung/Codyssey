import os

LOG_FILE = "data/mission_computer_main.log"
ERROR_LOG_FILE = "1-week/error_log.log"
REPORT_FILE = "1-week/log_analysis.md"

ERROR_KEYWORDS = ["unstable", "explosion", "powered down"]

def read_log_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        logs = file.readlines()
        return logs

def analyze_logs(logs):
    error_lines = [line for line in logs if any(keyword in line for keyword in ERROR_KEYWORDS)]

    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("# 로그 분석 보고서\n\n")
        report.write("## 주요 오류 로그 분석\n\n")
        
        for line in error_lines:
            report.write(f"- {line.strip()}\n")

    return error_lines

def save_error_logs(error_lines):
    if error_lines:
        with open(ERROR_LOG_FILE, "w", encoding="utf-8") as error_file:
            error_file.writelines(error_lines)
        print(f"문제 로그 '{ERROR_LOG_FILE}' 저장")
    else:
        print("문제 로그 없음")

def reverse_logs_and_print(logs):
    print("\n=== 로그 파일 역순 출력 ===")
    for line in reversed(logs[1:]):
        print(line.strip())

def main():
    print("Hello Mars\n") 

    logs = read_log_file(LOG_FILE)

    if logs:
        error_logs = analyze_logs(logs)
        save_error_logs(error_logs)
        reverse_logs_and_print(logs)

if __name__ == "__main__":
    main()