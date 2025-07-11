from loguru import logger
import maliang
import time


class OakStorePage():
    def Home(self, cv, windows=None, page_type="oak"):
        """
        cv: 父画布
        windows: 父窗口
        page_type: 页面类型; "osk"=常规，"embed"=嵌入
        """
        StorePage = OakStorePage()
        cv.clear()

        # time.sleep(2)
        maliang.Image(cv, (0, 0), image=maliang.PhotoImage(file="./img/StoreHome/CW.png").resize(750, 395))
        maliang.Text(cv, (20, 385), text="ClassWidgets，一款美观实用的课程表软件。", anchor="sw")
        maliang.Button(cv, (730, 385), text="查看详情 >", anchor="se")
        maliang.Button(cv, (375, 420), text="进入商店", anchor="center", command=lambda: StorePage.page1(cv))

    def page1(self, cv, windows=None, page_type="oak"):
        StorePage = OakStorePage()
        Sector = SoftwareSector()
        cv.clear()

        maliang.Button(cv, (0, 0), text=" < ", command=lambda: StorePage.Home(cv))
        maliang.Text(cv, (50, 5), text="OakStore", fontsize=24)
        Sector.ClassWidgetsMini(cv, 85, 50)


class SoftwareSector():
    def ClassWidgetsMini(self, cv, position_x, position_y):
        Sector = SoftwareSector()
        Border = maliang.Label(cv, (position_x - 15, position_y - 5), size=(600, 75))
        Logo = maliang.Image(cv, (position_x, position_y), image=maliang.PhotoImage(file="./img/Page/Classwidgets.png").resize(64, 64))
        SoftwareName = maliang.Text(cv, (position_x + 75, position_y + 5), text="Class Widgets")
        Description = maliang.Text(cv, (position_x + 75, position_y + 35), text="全新桌面课程表", fontsize=16)
        DetailedInformation = maliang.Button(cv, (position_x + 475, position_y + 15), text="查看详情", command=lambda: Sector.ClassWidgets(cv)).disable(False)

    def ClassWidgets(self, cv):
        ClassWidgetsPage = maliang.Canvas(cv)
        ClassWidgetsPage.place(width=750, height=450)

        close = maliang.Button(ClassWidgetsPage, (0, 0), text=" × ", command=lambda: ClassWidgetsPage.destroy())
        title = maliang.Text(ClassWidgetsPage, (50, 5), text="Class Widgets 的详情页", fontsize=24)
        maliang.Image(ClassWidgetsPage, (40, 70), image=maliang.PhotoImage(file="./img/Page/Classwidgets.png").resize(128, 128))
        maliang.Text(ClassWidgetsPage, (200, 80), text="Class Widgets", fontsize=26)
        maliang.Label(ClassWidgetsPage, (200, 120), text="AIWB | 课程表 | 实用 | 美化", fontsize=16)
        maliang.Text(ClassWidgetsPage, (200, 160), text="全新桌面课程表")
        maliang.Label(ClassWidgetsPage, (40, 200), text="""详细信息：
开发者/商：RinLit
开源协议：GPL-3.0 license
""", fontsize=14)
