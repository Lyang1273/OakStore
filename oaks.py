from loguru import logger
import maliang
import time
import tomllib


def card(cv, position_x, position_y, name, description, icon_path):    # 一个信息展示小卡片
    maliang.Label(cv, (position_x-5, position_y-5), size=(300, 70))
    maliang.Image(cv, (position_x, position_y), image=maliang.PhotoImage(file=icon_path).resize(64, 64))
    maliang.Text(cv, (position_x+75, position_y), text=name, fontsize=24)
    maliang.Text(cv, (position_x+75, position_y+35), text=description, fontsize=16)

# 想吃RinLit了qwq
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
        maliang.Text(cv, (40, 10), text="推荐的软件", fontsize=24)
        card(cv, 50, 60, "Class Widgets", "全新桌面课程表", "./img/Page/ClassWidgets.png")
        card(cv, 50, 140, "ClassIsland", "课表的信息显示工具", "./img/Page/ClassIsland.png")

        maliang.Text(cv, (710, 10), text="OakStore", fontsize=24, anchor="ne")
        maliang.Button(cv, (700, 60), text="进入商店以查看更多", anchor="ne", command=lambda: StorePage.page1(cv), fontsize=16)
        maliang.Button(cv, (700, 110), text="OakStore设置", anchor="ne", fontsize=16)
        maliang.Button(cv, (700, 160), text="关于OakStore", anchor="ne", fontsize=16)

    def about(self, cv, page_type="oak"):
        cv.clear()
        StorePage = OakStorePage()

        maliang.Button(cv, (0, 0), text=" < ", command=lambda: StorePage.Home(cv))
        maliang.Text(cv, (10, 50), )

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


class SoftwareInfo():
    def GetSoftwareInformationList(self, name):    # 获取软件信息
        logger.info(f"获取{name}的软件信息")
        with open("./config/StorePage/SoftwareInformationList.toml", "rb") as f:
            Info = tomllib.load(f)

            SwName = Info["name"]    # 软件名
            SwDeveloper = Info["developer"]    # 开发者
            SwOpenSourceLicense = Info["openSourceLicense"]    # 开源协议
            SwDevelopmentStatus = Info["developmentStatus"]    # 开发状态
            SwProgrammingLanguage = Info["programmingLanguage"]     # 编程语言
            SwOfficialWebsite = Info["officialWebsite"]    # 官网
