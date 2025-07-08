import os
import datetime
from loguru import logger

# 创建日志目录（logs）
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期和时间yyyy-mm-dd HH:MM:SS
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H`%M`%S")
# 设置日志文件名为当前日期和时间
log_file_name = f"{time_now}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# 配置日志
logger.add(log_file_path, level='DEBUG', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {module} | {message}')

logger.info("日志配置完成")


logger.debug("加载核心")
import core


def main():
    logger.info("OakStore启动……")
    logger.debug("我已出舱，感觉良好。")
    logger.info("启动核心")

    logger.debug("实例化 core.Application")
    APP = core.Application()
    logger.info("创建主窗口")
    APP.GUI()
