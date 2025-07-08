from loguru import logger

logger.debug("导入maliang")
import maliang


class Application:
    def GUI(self):
        logger.debug("创建主窗口")
        root = maliang.Tk(size=(750, 450))

        logger.info("进入主循环")
        root.mainloop()
