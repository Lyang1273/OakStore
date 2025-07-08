import main

import os
import datetime

import requests
import maliang
import loguru
from loguru import logger


# 启动器日志目录
log_dir = 'LauncherLogs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期和时间yyyy-mm-dd HH:MM:SS
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H`%M`%S")
# 设置日志文件名为当前日期和时间
log_file_name = f"{time_now}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# 配置日志
logger.add(log_file_path, level='DEBUG', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}')

logger.info("启动器日志配置完成")


def run():
    logger.debug("启动主程序")
    main.main()


if __name__ == "__main__":
    run()
