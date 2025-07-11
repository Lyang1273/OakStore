from loguru import logger

logger.debug("导入maliang")
import maliang
logger.debug("导入商店界面")
import oaks

logger.debug("实例化")
OAKSGUI = oaks.OakStorePage()


class Application:
    def GUI(self):
        logger.debug("创建主窗口")
        root = maliang.Tk(size=(750, 450), title="OakStore")

        logger.debug("创建启动界面")
        setup = maliang.Toplevel(root, size=(500, 250), title="启动")
        setup.center()
        setup_cv = maliang.Canvas(setup)
        setup_cv.place(width=500, height=250)
        maliang.Text(setup_cv, (20, 20), text="正在启动中")

        logger.info("居中主窗口")
        root.center()
        logger.info("创建画布")
        cv = maliang.Canvas(root, free_anchor=False, auto_zoom=True)
        cv.place(width=750, height=450)
        OAKSGUI.Home(cv, root)

        logger.info("进入主循环")
        setup.destroy()
        root.mainloop()
